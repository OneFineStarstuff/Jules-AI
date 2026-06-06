import unittest
from src.governance_engine.fiduciary_guardrail_engine import FiduciaryGuardrailEngine

class TestFiduciary(unittest.TestCase):
    def setUp(self):
        self.engine = FiduciaryGuardrailEngine()

    def test_mas_feat_violation(self):
        intent = {"impact": "HIGH", "human_oversight": False}
        result = self.engine.enforce_policy(intent)
        self.assertEqual(result["decision"], "DENY")
        self.assertEqual(result["reason"], "MAS_FEAT_ARTICLE_14_VIOLATION")

    def test_consumer_duty_outcome(self):
        intent = {"customer_type": "RETAIL", "risk": 0.6}
        result = self.engine.enforce_policy(intent)
        self.assertEqual(result["decision"], "DENY")
        self.assertEqual(result["reason"], "CONSUMER_DUTY_OUTCOME_FAIL")

    def test_allow_nominal(self):
        intent = {"impact": "LOW", "customer_type": "INSTITUTIONAL", "risk": 0.1}
        result = self.engine.enforce_policy(intent)
        self.assertEqual(result["decision"], "ALLOW")

if __name__ == "__main__":
    unittest.main()
