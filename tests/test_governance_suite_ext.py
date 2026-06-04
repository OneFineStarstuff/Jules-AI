import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.governance_engine.reflexive_treaty_engine import ReflexiveTreatyEvolutionEngine
from src.governance_engine.fiduciary_guardrail_engine import FiduciaryGuardrailEngine

class TestGovernanceSuiteExt(unittest.TestCase):
    def test_treaty_evolution(self):
        engine = ReflexiveTreatyEvolutionEngine()
        res = engine.evolve_logic("APAC", "MAS_FEAT_UPDATE")
        self.assertEqual(res["status"], "APPLIED_TO_GDL")

    def test_fiduciary_enforcement(self):
        engine = FiduciaryGuardrailEngine()
        trade = {"risk_delta": 0.01, "has_cot_trace": True}
        valid, msg = engine.validate_trade(trade)
        self.assertTrue(valid)

if __name__ == "__main__":
    unittest.main()
