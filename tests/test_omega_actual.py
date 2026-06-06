import unittest
from src.governance_engine.omega_actual import OmegaActualTreatyEngine

class TestOmegaActual(unittest.TestCase):
    def setUp(self):
        self.engine = OmegaActualTreatyEngine()

    def test_consensus_check(self):
        report = self.engine.verify_consensus()
        self.assertIn("consensus", report)
        self.assertIn("timestamp", report)

    def test_planetary_limits(self):
        # Within limits
        report = self.engine.check_planetary_limits(10**25)
        self.assertEqual(report["status"], "COMPLIANT")

        # Exceed limits
        report = self.engine.check_planetary_limits(10**27)
        self.assertEqual(report["status"], "MASTER_SHUTDOWN_INITIATED")
        self.assertFalse(self.engine.switch_armed)

if __name__ == "__main__":
    unittest.main()
