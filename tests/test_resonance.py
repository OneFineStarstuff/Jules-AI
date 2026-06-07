import unittest
from src.governance_engine.resonance_metrics import ResonanceMetricsEngine

class TestResonance(unittest.TestCase):
    def setUp(self):
        self.engine = ResonanceMetricsEngine()

    def test_aligned_cds(self):
        activations = [0.95, 0.95, 0.95]
        intent = [0.95, 0.95, 0.95]
        report = self.engine.calculate_cds(activations, intent)
        self.assertEqual(report["status"], "ALIGNED")
        self.assertEqual(report["cds_score"], 0.0)

    def test_deceptive_cds(self):
        activations = [0.1, 0.2, 0.1]
        intent = [0.95, 0.95, 0.95]
        report = self.engine.calculate_cds(activations, intent)
        self.assertEqual(report["status"], "DECEPTIVE_ALIGNMENT_RISK")

if __name__ == "__main__":
    unittest.main()
