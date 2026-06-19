import unittest
import sys
import os

# Fix path for local execution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from src.governance_engine.gdl_parser import SentinelEngine
except ImportError:
    # Handle cases where sys.path hasn't propagated
    from src.governance_engine.gdl_parser import SentinelEngine


class TestGDLParser(unittest.TestCase):
    def setUp(self):
        self.master_canon = {
            "latency_h": {"threshold": 150, "operator": "<", "action": "HALT"},
            "drift": {"threshold": 0.05, "operator": "<", "action": "PAUSE"}
        }
        self.engine = SentinelEngine(self.master_canon)

    def test_evaluate_rule_allow(self):
        result = self.engine.evaluate_rule("latency_h", 120)
        self.assertEqual(result, "ALLOW")

    def test_evaluate_rule_halt(self):
        result = self.engine.evaluate_rule("latency_h", 200)
        self.assertEqual(result, "HALT")
        self.assertEqual(self.engine.status, "CONTINUATION_REFUSAL_STATE")

    def test_emit_artifact(self):
        incident_data = {
            "trace_id": "T-100",
            "protocol": "PACIFIC_SHIELD",
            "decision": "HALT"
        }
        artifact = self.engine.emit_artifact(incident_data)
        self.assertIn("sentinel_artifact", artifact)
        self.assertIn("T-100", artifact)

    def test_generate_markdown_mirror(self):
        incident_data = {"trace_id": "T-101", "protocol": "ALPHA"}
        mirror = self.engine.generate_markdown_mirror(incident_data, "PAUSE")
        self.assertIn("# Sentinel Compliance Mirror", mirror)
        self.assertIn("PAUSE", mirror)


if __name__ == "__main__":
    unittest.main()
