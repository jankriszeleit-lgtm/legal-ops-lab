# Work Plan DOCX host adapter

This executable reference adapter implements the output boundary in
Implementation §12.1. It uses Python 3.10+ and the standard library. It does not
run the Planner, store plan status, import Word, send messages or provide a web
server. Code and fixtures use the repository's CC BY 4.0 license.

## Bind to a host

On **every** successful creation/update, including LIGHT plans and mid-run
corrections:

1. Finish the existing canonical write/QC and freeze the complete professional
   plan. Keep its native schema, stable IDs and revision values. Do not pass a
   chat summary, delta, whole RunRecord, internal configuration or telemetry.
2. Resolve both capabilities against the actual host. The bundled writer
   supplies generation only where Python/code and permitted file output exist.
   The host must separately supply permitted, working download/attachment
   delivery. A file path, `FILE_ACCESS`, or a Boolean guessed by a prompt is
   insufficient evidence. Configuration defaults remain `UNKNOWN`.
3. Invoke `export_work_plan` with the authoritative JSON file and the real
   delivery callback. Keep the source frozen/locked through generation and
   delivery. The adapter checks for source changes before and after delivery;
   concurrency control remains the host's responsibility.
4. Present the existing canonical output regardless of the result. Append the
   returned `download_reference` **only** for `EXPORTED`. For `UNAVAILABLE` or
   `FAILED`, show `reason`, with no previous download as current. Keep the
   receipt outside canonical plan data. Retain no extra event/status registry.

```python
from work_plan_docx import Capabilities, export_work_plan

# Called from the host's existing post-freeze output hook; no extra user opt-in.
# These values and attach_download are supplied by the verified host adapter.
result = export_work_plan(
    canonical_plan_path,
    permitted_output_directory,
    capabilities=Capabilities(
        generate_docx=verified_generation_capability,  # "YES" / "NO" / "UNKNOWN"
        deliver_file=verified_delivery_capability,
    ),
    deliver_file=attach_download,
)
# attach_download(path) must publish/attach this actual file in the permitted
# current output surface and return its real user-accessible reference, or raise.
# Always render the canonical output. Render result.download_reference only
# when result.status == "EXPORTED"; otherwise render result.reason.
```

There is deliberately no CLI that turns a local path into a purported download.
A host without an attachment mechanism must return `UNAVAILABLE`. Native file
export hosts may implement the same boundary using their own writer and
existing canonical format; the Python adapter is not a mandatory new runtime.

## Input and output contract

Input is the host's existing **JSON object containing the professional plan**.
All keys, nested fields and list entries are rendered as labelled, indented
editable Word paragraphs, including extensions, unknowns, empty collections
and nulls. No new required plan schema is imposed. The fixture is a synthetic
example, not a new canonical data contract. Arbitrary non-JSON sources are not
supported by this reference writer; use the native host's adapter for those.

For front matter only, default metadata bindings read root `plan_id`, `version`,
`as_of` and `commit_sha`. To bind existing nested names without changing them:

```python
metadata_paths = {
    "plan_id": ("identity", "key"),
    "version": ("identity", "revision"),
}
```

Pass that mapping to `export_work_plan`. Missing values are `UNKNOWN`. A source
path, SHA-256 over exact source bytes, and actual UTC generation date always
appear. The digest identifies unversioned/reused-version snapshots without
inventing plan or run IDs. Generation time is export provenance, not plan time.
No extra metadata is written back to the source.

Names follow
`work-plan_<safe-plan-id>_<safe-version>_<source-digest-prefix>_NON_CANONICAL.docx`.
Different snapshots get different names. The full digest is inside the file.
Re-exporting the same snapshot replaces its derived file atomically; exporting
a revision does not overwrite an earlier revision's file. Old files may remain
on disk under the host's retention policy but are never returned as current
on a failed attempt. A callback can have partially attached a file before
failing; the host must suppress/retract that link if needed. There is no
cross-system delivery transaction in this reference adapter.

Duplicate JSON keys, invalid JSON/XML characters and invalid numbers fail
explicitly rather than dropping canonical information. The adapter validates
the ZIP/XML package before calling delivery. The host must test its actual
Word client and download route before marking the integration conformant.

The visible notice is fixed:

> Nicht-kanonische Lesefassung. Maßgeblich ist der kanonische Work Plan.

Word edits never feed back. A subsequent explicit canonical revision follows
the existing Planner correction/replan rules and regenerates the derivative.
Plan output remains subject to the current permission/data-zone rules; this
adapter grants no external sharing authority.

## Reproducible checks

From the repository root:

```sh
python3 -m unittest discover -s legal-work-planner/releases/2026-11-17/05_HOST_ADAPTER/tests -v
```

The tests use synthetic data and temporary files. They check real DOCX package
structure, all fixture content, provenance, filenames, source immutability,
complete replan output, unavailable capabilities, generation/delivery failures,
source races and the unchanged Core observability block. Delivery is a test
double; no production host or Planner/model run is implied. The CI suite also
opens the output with the independent `python-docx` reader.

D-01–D-06 in [`TESTING_AND_PILOTS.md`](../03_TESTING/TESTING_AND_PILOTS.md)
remain required for each real host binding. Report unrun host/model tests as
`UNVERIFIED`, never PASS from a unit test or prompt presence.
