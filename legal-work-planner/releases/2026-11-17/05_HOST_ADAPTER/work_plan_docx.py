"""One-way DOCX output for a frozen JSON professional plan (CC-BY-4.0).

No planning, canonical writes, imports, telemetry, network or persistent export
registry. The host owns permission and the real attachment/download callback.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
from tempfile import NamedTemporaryFile
from typing import Callable, Mapping
from xml.etree import ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile

NOTICE = "Nicht-kanonische Lesefassung. Maßgeblich ist der kanonische Work Plan."
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/package/2006/relationships"
CT = "http://schemas.openxmlformats.org/package/2006/content-types"
ET.register_namespace("w", W)


@dataclass(frozen=True)
class Capabilities:
    generate_docx: str = "UNKNOWN"
    deliver_file: str = "UNKNOWN"


@dataclass(frozen=True)
class ExportResult:
    canonical_reference: str
    status: str
    source_sha256: str | None = None
    download_reference: str | None = None
    reason: str | None = None


def _xml(root: ET.Element) -> bytes:
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def _text(value: object) -> str:
    return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)


def _paragraph(body: ET.Element, text: str, *, bold: bool = False, depth: int = 0) -> None:
    # Reject invalid XML characters instead of silently dropping canonical text.
    if any(not (c in "\t\n\r" or 0x20 <= ord(c) <= 0xD7FF
                or 0xE000 <= ord(c) <= 0xFFFD or 0x10000 <= ord(c) <= 0x10FFFF)
           for c in text):
        raise ValueError("Plan contains characters that XML 1.0 cannot represent")
    p = ET.SubElement(body, f"{{{W}}}p")
    props = ET.SubElement(p, f"{{{W}}}pPr")
    ET.SubElement(props, f"{{{W}}}ind", {f"{{{W}}}left": str(min(depth, 12) * 240)})
    ET.SubElement(props, f"{{{W}}}spacing", {f"{{{W}}}after": "100"})
    run = ET.SubElement(p, f"{{{W}}}r")
    if bold:
        ET.SubElement(ET.SubElement(run, f"{{{W}}}rPr"), f"{{{W}}}b")
    for part in re.split(r"(\r\n|\n|\t|\r)", text):
        if part in ("\r\n", "\n", "\r"):
            ET.SubElement(run, f"{{{W}}}br")
        elif part == "\t":
            ET.SubElement(run, f"{{{W}}}tab")
        else:
            ET.SubElement(run, f"{{{W}}}t", {"{http://www.w3.org/XML/1998/namespace}space": "preserve"}).text = part


def _content(body: ET.Element, label: str, value: object, depth: int = 0) -> None:
    """Render every key/value, including extensions, nulls and empty containers."""
    if isinstance(value, (dict, list)) and value:
        _paragraph(body, label, bold=True, depth=depth)
        entries = value.items() if isinstance(value, dict) else enumerate(value, 1)
        for key, child in entries:
            _content(body, str(key), child, depth + 1)
    else:
        _paragraph(body, f"{label}: {_text(value)}", depth=depth)


def _metadata(plan: dict, paths: Mapping[str, tuple[str, ...]] | None) -> dict[str, str]:
    bindings = {key: (key,) for key in ("plan_id", "version", "as_of", "commit_sha")}
    bindings.update(paths or {})
    result = {}
    for label, path in bindings.items():
        value = plan
        for key in path:
            value = value.get(key) if isinstance(value, dict) else None
        result[label] = _text(value) if value is not None and value != "" else "UNKNOWN"
    return result


def _component(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-")[:40] or "UNKNOWN"


def _write_docx(path: Path, plan: dict, source: str, digest: str, metadata: dict) -> None:
    document = ET.Element(f"{{{W}}}document")
    body = ET.SubElement(document, f"{{{W}}}body")
    _paragraph(body, "Work Plan — Non-canonical reading copy", bold=True)
    _paragraph(body, NOTICE, bold=True)
    _paragraph(body, "One-way export. Word edits do not update the canonical Work Plan.")
    _paragraph(body, f"Source: {source}")
    for key, value in metadata.items():
        _paragraph(body, f"{key}: {value}")
    _paragraph(body, f"Source SHA-256: {digest}")
    _paragraph(body, f"Generated (UTC): {datetime.now(timezone.utc).isoformat()}")
    _content(body, "Complete canonical professional plan", plan)
    section = ET.SubElement(body, f"{{{W}}}sectPr")
    ET.SubElement(section, f"{{{W}}}pgSz", {f"{{{W}}}w": "11906", f"{{{W}}}h": "16838"})
    ET.SubElement(section, f"{{{W}}}pgMar", {f"{{{W}}}top": "1134", f"{{{W}}}bottom": "1134",
                                          f"{{{W}}}left": "1134", f"{{{W}}}right": "1134"})
    types = ET.Element("Types", xmlns=CT)
    ET.SubElement(types, "Default", Extension="rels", ContentType="application/vnd.openxmlformats-package.relationships+xml")
    ET.SubElement(types, "Default", Extension="xml", ContentType="application/xml")
    ET.SubElement(types, "Override", PartName="/word/document.xml",
                  ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml")
    relationships = ET.Element("Relationships", xmlns=R)
    ET.SubElement(relationships, "Relationship", Id="rId1",
                  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument",
                  Target="word/document.xml")
    with ZipFile(path, "w", ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", _xml(types))
        archive.writestr("_rels/.rels", _xml(relationships))
        archive.writestr("word/document.xml", _xml(document))


def _validate_docx(path: Path) -> None:
    # Validate the actual output independently of the writer before delivery.
    with ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise ValueError("Corrupt DOCX package")
        types = ET.fromstring(archive.read("[Content_Types].xml"))
        if not any(e.get("PartName") == "/word/document.xml" and e.get("ContentType") ==
                   "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
                   for e in types):
            raise ValueError("Missing Word document content type")
        relationships = ET.fromstring(archive.read("_rels/.rels"))
        if not any(e.get("Target") == "word/document.xml" and e.get("Type") ==
                   "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
                   for e in relationships):
            raise ValueError("Missing Word document relationship")
        document = ET.fromstring(archive.read("word/document.xml"))
        if document.tag != f"{{{W}}}document" or document.find(f"{{{W}}}body") is None:
            raise ValueError("Missing Word document body")
        for name in archive.namelist():
            ET.fromstring(archive.read(name))


def _unique_object(pairs: list) -> dict:
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f"Duplicate canonical JSON key: {key}")
        obj[key] = value
    return obj


def _invalid_number(value: str) -> None:
    raise ValueError(f"Invalid JSON number: {value}")


class _JsonNumber(str):
    """Preserve exact numeric text, including decimal precision and exponents."""


def export_work_plan(
    canonical_path: str | Path,
    output_dir: str | Path,
    *,
    capabilities: Capabilities = Capabilities(),
    deliver_file: Callable[[Path], str] | None = None,
    metadata_paths: Mapping[str, tuple[str, ...]] | None = None,
) -> ExportResult:
    """Export the entire JSON plan and deliver it through a verified host route.

    Call after every canonical freeze, including revisions. The callback must
    return a real user-accessible reference after successful delivery, or raise.
    The host must hold the canonical snapshot stable until this call returns.
    Paths only select existing provenance fields; they never change plan data.
    """
    source = Path(canonical_path).resolve()
    reference = str(source)
    missing = []
    if capabilities.generate_docx != "YES":
        missing.append("work_plan.generate_docx")
    if capabilities.deliver_file != "YES" or deliver_file is None:
        missing.append("work_plan.deliver_file")
    if missing:
        return ExportResult(reference, "UNAVAILABLE", reason="Unavailable: " + ", ".join(missing))
    digest = None
    temporary = None
    try:
        raw = source.read_bytes()
        digest = sha256(raw).hexdigest()
        plan = json.loads(raw, object_pairs_hook=_unique_object, parse_constant=_invalid_number,
                          parse_float=_JsonNumber, parse_int=_JsonNumber)
        if not isinstance(plan, dict):
            raise ValueError("Expected a JSON object containing the professional plan")
        metadata = _metadata(plan, metadata_paths)
        filename = (f"work-plan_{_component(metadata['plan_id'])}_{_component(metadata['version'])}_"
                    f"{digest[:16]}_NON_CANONICAL.docx")
        directory = Path(output_dir).resolve()
        directory.mkdir(parents=True, exist_ok=True)
        destination = directory / filename
        if destination == source:
            raise ValueError("DOCX destination must not replace canonical source")
        with NamedTemporaryFile(dir=directory, suffix=".docx", delete=False) as tmp:
            temporary = Path(tmp.name)
        _write_docx(temporary, plan, reference, digest, metadata)
        _validate_docx(temporary)
        if source.read_bytes() != raw:
            raise ValueError("Canonical source changed during export; export the current snapshot again")
        os.replace(temporary, destination)
        temporary = None
        download = deliver_file(destination)
        if not isinstance(download, str) or not download.strip():
            raise ValueError("Host did not return a download reference")
        if source.read_bytes() != raw:
            raise ValueError("Canonical source changed during delivery; do not present this export as current")
        return ExportResult(reference, "EXPORTED", digest, download)
    except Exception as error:
        # An export failure must never roll back/block the canonical plan output.
        return ExportResult(reference, "FAILED", digest, reason=f"DOCX export failed: {error}")
    finally:
        if temporary is not None:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass  # Host retention/cleanup must not prevent canonical output.
