# SPDX-License-Identifier: Apache-2.0
"""Synthetic artifact/adapter checks. No claims about an LLM or live host."""
from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from xml.etree import ElementTree as ET
from zipfile import ZipFile

ADAPTER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ADAPTER))
import work_plan_docx as exporter
try:
    from docx import Document
except ImportError:
    Document = None


class WorkPlanDocxTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.source = self.root / 'canonical.json'
        self.original = (Path(__file__).with_name('plan.json')).read_bytes()
        self.source.write_bytes(self.original)
        self.output = self.root / 'output'
        self.delivered = []

    def deliver(self, path):
        # Synthetic host delivery: inspect the actual file, then return a receipt.
        self.assertTrue(path.is_file())
        self.delivered.append(path)
        return 'test-download://' + path.name

    def export(self, **overrides):
        args = dict(capabilities=exporter.Capabilities('YES', 'YES'), deliver_file=self.deliver)
        args.update(overrides)
        return exporter.export_work_plan(self.source, self.output, **args)

    def paragraphs(self, path):
        with ZipFile(path) as package:
            self.assertIsNone(package.testzip())
            self.assertEqual(set(package.namelist()), {'[Content_Types].xml', '_rels/.rels', 'word/document.xml'})
            types = ET.fromstring(package.read('[Content_Types].xml'))
            self.assertTrue(any(e.get('PartName') == '/word/document.xml' and
                                e.get('ContentType').endswith('wordprocessingml.document.main+xml')
                                for e in types))
            relationships = ET.fromstring(package.read('_rels/.rels'))
            self.assertEqual(relationships[0].get('Target'), 'word/document.xml')
            self.assertTrue(relationships[0].get('Type').endswith('/officeDocument'))
            document = ET.fromstring(package.read('word/document.xml'))
        return [''.join(p.itertext()) for p in document.iter(f'{{{exporter.W}}}p')]

    def test_real_docx_contains_all_plan_fields_and_provenance(self):
        result = self.export()
        self.assertEqual(result.status, 'EXPORTED')
        path, = self.delivered
        paragraphs = self.paragraphs(path)
        text = '\n'.join(paragraphs)
        # Every nested key and scalar is retained, including extension fields.
        def check(value):
            if isinstance(value, dict):
                for key, item in value.items():
                    self.assertIn(key, text)
                    check(item)
            elif isinstance(value, list):
                for item in value:
                    check(item)
            else:
                expected = value if isinstance(value, str) else json.dumps(value)
                for part in expected.replace('\t', '\n').splitlines():
                    self.assertIn(part, text)
        check(json.loads(self.original))
        self.assertIn(exporter.NOTICE, text)
        self.assertIn('Source: ' + str(self.source), text)
        self.assertIn('version: r1', text)
        self.assertIn('as_of: 2026-11-17T12:00:00Z', text)
        self.assertIn('commit_sha: 1234567890abcdef1234567890abcdef12345678', text)
        digest = sha256(self.original).hexdigest()
        self.assertIn('Source SHA-256: ' + digest, text)
        generated = next(p.removeprefix('Generated (UTC): ') for p in paragraphs if p.startswith('Generated (UTC): '))
        self.assertIsNotNone(datetime.fromisoformat(generated).tzinfo)
        self.assertEqual(result.source_sha256, digest)
        self.assertEqual(path.name, f'work-plan_PL-002_r1_{digest[:16]}_NON_CANONICAL.docx')
        self.assertEqual(result.download_reference, 'test-download://' + path.name)
        self.assertEqual(self.source.read_bytes(), self.original)

    @unittest.skipIf(Document is None, "Independent reader requires python-docx (installed in CI)")
    def test_independent_word_reader_opens_the_document(self):
        self.export()
        document = Document(self.delivered[-1])
        text = "\n".join(p.text for p in document.paragraphs)
        for value in (exporter.NOTICE, "WI-01", "status: IN_PROGRESS", "D-01", "Änderung"):
            self.assertIn(value, text)
        self.assertEqual(len(document.sections), 1)

    def test_invalid_generated_package_is_not_delivered(self):
        def corrupt(path, *_):
            path.write_bytes(b"not a DOCX")
        with patch.object(exporter, "_write_docx", side_effect=corrupt):
            result = self.export()
        self.assertEqual(result.status, "FAILED")
        self.assertIsNone(result.download_reference)
        self.assertFalse(self.delivered)
        self.assertEqual(self.source.read_bytes(), self.original)

    def test_replan_exports_complete_current_snapshot_with_stable_ids(self):
        first = self.export()
        old_path = self.delivered[-1]
        old_docx = old_path.read_bytes()
        revised = json.loads(self.original)
        revised['version'] = 'r2'
        revised['work_items'][0]['status'] = 'DONE'
        revised['work_items'][1]['priority'] = 'HIGH'
        revised['next_steps'] = ['Resolve D-01']
        revised['replan_delta'] = 'WI-01 finished; WI-02 now urgent'
        self.source.write_text(json.dumps(revised, ensure_ascii=False))
        frozen = self.source.read_bytes()
        second = self.export()
        self.assertEqual(second.status, 'EXPORTED')
        self.assertNotEqual(first.download_reference, second.download_reference)
        text = '\n'.join(self.paragraphs(self.delivered[-1]))
        for required in ('version: r2', 'status: DONE', 'WI-01', 'WI-02', revised['goal'], revised['done_when']):
            self.assertIn(required, text)
        self.assertNotIn('status: IN_PROGRESS', text)
        self.assertEqual(old_path.read_bytes(), old_docx)
        self.assertEqual(self.source.read_bytes(), frozen)

    def test_missing_unknown_and_false_capabilities_fail_closed(self):
        for capability in ('NO', 'UNKNOWN', '', None, True):
            for caps in (exporter.Capabilities(capability, 'YES'), exporter.Capabilities('YES', capability)):
                with self.subTest(caps=caps):
                    result = self.export(capabilities=caps)
                    self.assertEqual(result.status, 'UNAVAILABLE')
                    self.assertIsNone(result.download_reference)
                    self.assertIn('work_plan.', result.reason)
        self.assertEqual(self.export(deliver_file=None).status, 'UNAVAILABLE')
        self.assertFalse(self.output.exists())
        self.assertFalse(self.delivered)
        self.assertEqual(self.source.read_bytes(), self.original)

    def test_generation_and_delivery_failures_keep_canonical_output(self):
        with patch.object(exporter, '_write_docx', side_effect=OSError('disk full')):
            failed = self.export()
        self.assertEqual(failed.status, 'FAILED')
        self.assertIn('disk full', failed.reason)
        self.assertEqual(list(self.output.iterdir()), [])
        for delivery in (lambda _: '', lambda _: None):
            with self.subTest(delivery=delivery):
                failed = self.export(deliver_file=delivery)
                self.assertEqual(failed.status, 'FAILED')
                self.assertIsNone(failed.download_reference)
        def broken_delivery(_):
            raise OSError('attachment unavailable')
        failed = self.export(deliver_file=broken_delivery)
        self.assertEqual(failed.status, 'FAILED')
        self.assertIn('attachment unavailable', failed.reason)
        self.assertEqual(failed.canonical_reference, str(self.source))
        self.assertEqual(self.source.read_bytes(), self.original)

    def test_failed_revision_never_returns_previous_download(self):
        self.assertEqual(self.export().status, 'EXPORTED')
        self.source.write_text('{"plan_id":"PL-002", "version":"r2", "goal":"Revised"}')
        def unavailable(_):
            raise OSError('delivery failed')
        failed = self.export(deliver_file=unavailable)
        self.assertEqual(failed.status, 'FAILED')
        self.assertIsNone(failed.download_reference)
        self.assertNotEqual(failed.source_sha256, sha256(self.original).hexdigest())

    def test_unknown_metadata_and_same_version_content_are_distinguishable(self):
        self.source.write_text('{"goal":"First snapshot"}')
        self.export()
        first = self.delivered[-1]
        self.source.write_text('{"goal":"Corrected snapshot"}')
        self.export()
        second = self.delivered[-1]
        self.assertNotEqual(first.name, second.name)
        self.assertIn('UNKNOWN_UNKNOWN_', second.name)
        self.assertIn('version: UNKNOWN', '\n'.join(self.paragraphs(second)))

    def test_existing_nested_metadata_contract_is_supported_without_mutation(self):
        plan = {'identity': {'key': 'PL/custom', 'revision': 'rev:3'}, 'actions': [{'key': 'A-1', 'done': False}]}
        self.source.write_text(json.dumps(plan))
        frozen = self.source.read_bytes()
        result = self.export(metadata_paths={'plan_id': ('identity', 'key'), 'version': ('identity', 'revision')})
        self.assertEqual(result.status, 'EXPORTED')
        self.assertTrue(self.delivered[-1].name.startswith('work-plan_PL_custom_rev_3_'))
        self.assertIn('plan_id: PL/custom', '\n'.join(self.paragraphs(self.delivered[-1])))
        self.assertEqual(self.source.read_bytes(), frozen)

    def test_source_change_during_generation_is_rejected_before_delivery(self):
        real_writer = exporter._write_docx
        def change_source(*args):
            real_writer(*args)
            self.source.write_text('{"goal":"Newer plan"}')
        with patch.object(exporter, '_write_docx', side_effect=change_source):
            result = self.export()
        self.assertEqual(result.status, 'FAILED')
        self.assertIn('changed during export', result.reason)
        self.assertFalse(self.delivered)
        self.assertEqual(list(self.output.iterdir()), [])

    def test_source_change_during_delivery_is_not_reported_as_current(self):
        def change_source(_):
            self.source.write_text('{"goal":"Newer plan"}')
            return 'test-download://old-snapshot.docx'
        result = self.export(deliver_file=change_source)
        self.assertEqual(result.status, 'FAILED')
        self.assertIsNone(result.download_reference)

    def test_docx_edits_do_not_roundtrip(self):
        self.export()
        self.delivered[-1].write_bytes(b'Edited independently in Word')
        self.assertEqual(self.source.read_bytes(), self.original)
        self.assertEqual(self.export().status, 'EXPORTED')
        self.paragraphs(self.delivered[-1])

    def test_numeric_precision_and_large_exponents_are_preserved(self):
        self.source.write_text('{"budget":0.1234567890123456789012345,"large":1e400,"zero":-0}')
        result = self.export()
        self.assertEqual(result.status, 'EXPORTED')
        text = '\n'.join(self.paragraphs(self.delivered[-1]))
        for value in ('0.1234567890123456789012345', '1e400', 'zero: -0'):
            self.assertIn(value, text)

    def test_invalid_sources_fail_without_silent_content_loss(self):
        for raw in (b'{broken', b'[]', b'{"id":1,"id":2}', b'{"n": NaN}', b'{"goal":"bad\\u0001character"}'):
            with self.subTest(raw=raw):
                self.source.write_bytes(raw)
                result = self.export()
                self.assertEqual(result.status, 'FAILED')
                self.assertIsNone(result.download_reference)
                self.assertEqual(self.source.read_bytes(), raw)
        self.assertFalse(self.delivered)


class ReleaseContractTests(unittest.TestCase):
    def test_observability_snapshot_is_unchanged(self):
        release = ADAPTER.parent
        old = release.parent / '2026-08-27'
        def block(root):
            text = (root / '02_PROMPTS/PRT_PLANNER_CORE.md').read_text()
            return text.split('## 21. Run Observability contract\n', 1)[1].split('## 22.', 1)[0]
        self.assertEqual(block(release), block(old))


if __name__ == '__main__':
    unittest.main()
