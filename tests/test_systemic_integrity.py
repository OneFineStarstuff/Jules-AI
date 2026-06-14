import unittest
from src.infrastructure.zk_systemic_risk_proof import generate_gsri_zk_proof
from src.infrastructure.pqc_worm_logger import PQCWormLogger
from src.governance_engine.moe_stabilizer import MoEStabilizer

class TestSystemicIntegrity(unittest.TestCase):
    def test_gsri_zk_proof_generation(self):
        """Verifies that ZK-SNARK proofs can be generated for systemic risk."""
        proof_bundle = generate_gsri_zk_proof(0.093)
        self.assertEqual(proof_bundle["proof"]["protocol"], "Groth16")
        self.assertEqual(proof_bundle["public_signals"][1], 1) # Compliant

    def test_pqc_multi_algo_signing(self):
        """Verifies that the PQC logger utilizes multiple algorithms."""
        logger = PQCWormLogger()
        report = logger.verify_health()
        self.assertIn("ML-DSA-87", report["algorithms"])
        self.assertIn("SPHINCS+", report["algorithms"])

    def test_sara_moe_routing_stability(self):
        """Verifies that SARA boosts safety experts in MoE routing."""
        stabilizer = MoEStabilizer()
        probs = [0.1, 0.4, 0.2, 0.3]
        sara_probs = stabilizer.apply_sara_routing(probs)
        # Safety experts (0, 1, 2) should have higher relative weight
        self.assertTrue(sara_probs[0] > 0.1)

if __name__ == "__main__":
    unittest.main()
