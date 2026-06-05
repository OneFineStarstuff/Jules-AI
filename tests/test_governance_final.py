import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.governance_engine.omega_treaty_engine import OmegaActualTreatyEngine

class TestGovernanceFinal(unittest.TestCase):
    def test_omega_slashing(self):
        engine = OmegaActualTreatyEngine()
        report = {"gsri_score": 0.95, "metrics": {"node_id": "TEST-NODE"}}
        event = engine.check_breach_and_slash(report)
        self.assertEqual(event["event"], "BreachDetected")
        self.assertIn("TEST-NODE", engine.slashed_nodes)

if __name__ == "__main__":
    unittest.main()
