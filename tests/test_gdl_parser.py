import unittest
import sys
import os
import xml.etree.ElementTree as ET # nosec B405
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.governance_engine.gdl_parser import SentinelEngine

class TestSentinelEngine(unittest.TestCase):
    def setUp(self):
        self.canon = {
            "latency": {"threshold": 100, "operator": "<", "action": "HALT"},
            "bias": {"threshold": 0.90, "operator": ">", "action": "DENY"}
        }
        self.engine = SentinelEngine(self.canon)

    def test_evaluate_rule_allow(self):
        result = self.engine.evaluate_rule("latency", 50)
        self.assertEqual(result, "ALLOW")
        self.assertEqual(self.engine.status, "STEADY_GOVERNANCE_STATE")

    def test_evaluate_rule_violation(self):
        result = self.engine.evaluate_rule("latency", 150)
        self.assertEqual(result, "HALT")
        self.assertEqual(self.engine.status, "CONTINUATION_REFUSAL_STATE")

    def test_evaluate_rule_missing_metric(self):
        result = self.engine.evaluate_rule("unknown", 100)
        self.assertTrue(result) # Defaults to ALLOW/True

    def test_emit_artifact(self):
        incident_data = {"trace_id": "T1", "protocol": "TEST", "decision": "HALT"}
        xml_string = self.engine.emit_artifact(incident_data)
        root = ET.fromstring(xml_string) # nosec B314
        self.assertEqual(root.tag, "sentinel_artifact")
        self.assertEqual(root.find(".//trace_id").text, "T1")
        self.assertEqual(root.find(".//decision").text, "HALT")

    def test_generate_markdown_mirror(self):
        incident_data = {"trace_id": "T1", "protocol": "TEST", "decision": "HALT"}
        xml_string = self.engine.emit_artifact(incident_data)
        markdown = self.engine.generate_markdown_mirror(xml_string)
        self.assertIn("# Sentinel Compliance Mirror", markdown)
        self.assertIn("Final Decision:** HALT", markdown)

if __name__ == "__main__":
    unittest.main()
