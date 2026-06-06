import unittest
from src.governance_engine.rtee_engine import RTEEEngine
from src.governance_engine.gdl_parser import SentinelEngine

class TestRTEE(unittest.TestCase):
    def setUp(self):
        self.gdl = SentinelEngine({})
        self.engine = RTEEEngine(self.gdl)

    def test_synchronization(self):
        new_rules = {"new_metric": {"threshold": 100, "operator": "<", "action": "HALT"}}
        result = self.engine.synchronize_treaty("EU_G7_ACCORD", new_rules)
        self.assertEqual(result["status"], "TREATY_SYNCHRONIZED")
        self.assertEqual(self.gdl.master_canon["new_metric"]["threshold"], 100)
        self.assertEqual(self.engine.get_evolution_status()["total_evolutions"], 1)

if __name__ == "__main__":
    unittest.main()
