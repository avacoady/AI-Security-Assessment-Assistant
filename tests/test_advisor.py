import copy
import json
from pathlib import Path
import tempfile
import unittest

from advisor import EvidenceTools, demo_findings, ingest, run_agent, safe_cell, validate, write_reports

ROOT = Path(__file__).resolve().parents[1]


class AssessmentTests(unittest.TestCase):
    def setUp(self):
        self.evidence = ingest(ROOT / 'examples/client')
        self.findings = demo_findings(self.evidence)

    def test_fixture_distinguishes_missing_evidence(self):
        self.assertEqual({f['control']: f['status'] for f in self.findings}, {
            'MFA': 'documented_gap', 'ADMIN': 'documented_gap',
            'OFFBOARD': 'supported', 'REVIEW': 'unverified'})

    def test_fabricated_id_rejected(self):
        self.findings[0]['citations'][0]['id'] = 'invented'
        with self.assertRaises(ValueError):
            validate(self.findings, self.evidence, set(self.evidence))

    def test_fabricated_quote_rejected(self):
        self.findings[0]['citations'][0]['quote'] = 'MFA is enforced for every user.'
        with self.assertRaises(ValueError):
            validate(self.findings, self.evidence, set(self.evidence))

    def test_unretrieved_evidence_rejected(self):
        with self.assertRaises(ValueError):
            validate(self.findings, self.evidence, set())

    def test_duplicate_control_rejected(self):
        self.findings[1]['control'] = 'MFA'
        with self.assertRaises(ValueError):
            validate(self.findings, self.evidence, set(self.evidence))

    def test_unsupported_conclusion_rejected(self):
        self.findings[0]['citations'] = []
        with self.assertRaises(ValueError):
            validate(self.findings, self.evidence, set(self.evidence))

    def test_tools_do_not_read_arbitrary_paths(self):
        tools = EvidenceTools(self.evidence)
        self.assertEqual(tools.call('read_document', {'source': '/etc/passwd'}), [])
        with self.assertRaises(ValueError):
            tools.call('run_shell', {'command': 'whoami'})

    def test_symlink_not_ingested(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            (base / 'input').mkdir()
            (base / 'secret.txt').write_text('private')
            (base / 'input/link.txt').symlink_to(base / 'secret.txt')
            (base / 'input/normal.txt').write_text('normal')
            self.assertEqual([e['text'] for e in ingest(base / 'input').values()], ['normal'])

    def test_bounded_loop_on_malicious_action(self):
        calls = []
        def backend(messages):
            calls.append(1)
            return json.dumps({'action': 'tool', 'name': 'run_shell', 'arguments': {}})
        with self.assertRaisesRegex(ValueError, 'budget'):
            run_agent(self.evidence, backend, budget=3)
        self.assertEqual(len(calls), 3)

    def test_agent_retrieves_and_finishes_with_mock(self):
        actions = [dict(action='tool', name='read_document', arguments={'source': source})
                   for source in sorted({e['source'] for e in self.evidence.values()})]
        actions.append(dict(action='finish', findings=self.findings))
        results = iter(actions)
        findings, trace = run_agent(self.evidence, lambda messages: json.dumps(next(results)))
        self.assertEqual(findings, self.findings)
        self.assertEqual(trace[-1]['validation'], 'passed')

    def test_agent_recovers_from_bad_json(self):
        actions = ['not json'] + [json.dumps(dict(action='tool', name='read_document',
                                                 arguments={'source': source}))
                                  for source in sorted({e['source'] for e in self.evidence.values()})]
        actions.append(json.dumps(dict(action='finish', findings=self.findings)))
        results = iter(actions)
        _, trace = run_agent(self.evidence, lambda messages: next(results))
        self.assertIn('validation_error', trace[0])

    def test_csv_formula_escaped(self):
        for value in ['=HYPERLINK("x")', ' +1', '@SUM(1)', '-1']:
            self.assertTrue(safe_cell(value).startswith("'"))

    def test_reports_mark_human_review(self):
        with tempfile.TemporaryDirectory() as folder:
            write_reports(folder, self.findings, self.evidence, {'mode': 'test'}, [])
            report = (Path(folder) / 'report.md').read_text()
            self.assertIn('human review required', report)
            self.assertIn('2 documented gaps', report)
            self.assertTrue((Path(folder) / 'remediation.csv').exists())


if __name__ == '__main__':
    unittest.main()
