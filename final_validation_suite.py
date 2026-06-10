import unittest
import json
from omni_sentinel_24h_monitor import OmniSentinelMonitor
from src.governance_engine.omega_actual import OmegaActualTreatyEngine
from src.governance_engine.fiduciary_guardrail_engine import FiduciaryGuardrailEngine
from src.infrastructure.gien_relay import GIENRelay
from src.infrastructure.zk_verifier import ZKVerifier
from src.governance_engine.rtee_engine import RTEEEngine

class TestFinalValidation(unittest.TestCase):
    def setUp(self):
        self.monitor = OmniSentinelMonitor()

    def test_monitor_execution(self):
        """End-to-End verification of the 24h Governance Monitor."""
        summary = self.monitor.run_checks()
        self.assertEqual(summary["tpm_status"], "SUCCESS")
        self.assertEqual(summary["gsri_status"], "NOMINAL")
        self.assertEqual(summary["worm_health"], "HEALTHY")
        self.assertEqual(summary["relay_status"], "ONLINE")
        self.assertEqual(summary["zk_status"], "HEALTHY")

    def test_omega_actual_failsafe(self):
        """Verifies that OmegaActual triggers a fail-safe on FLOP violation."""
        engine = OmegaActualTreatyEngine()
        report = engine.verify_compute_compliance(10**27) # Over limit
        self.assertEqual(report["status"], "FAIL_SAFE_TRIGGERED")
        self.assertEqual(engine.treaty_status, "VIOLATION_DETECTED")

    def test_fiduciary_policy_enforcement(self):
        """Verifies that FiduciaryGuardrail rejects non-compliant transactions."""
        engine = FiduciaryGuardrailEngine()
        tx = {"bias_score": 0.1, "consumer_risk_level": 0.9} # Violates multiple
        report = engine.evaluate_transaction(tx)
        self.assertEqual(report["decision"], "REJECTED")
        self.assertIn("MAS_FEAT_BIAS_VIOLATION", report["violations"])

    def test_gien_node_id_security(self):
        """Verifies that GIEN nodes use 32-byte (64 char) secure hex IDs."""
        relay = GIENRelay()
        # Node ID format: NODE_<64_hex_chars>
        node_id_hex = relay.node_id.split("_")[1]
        self.assertEqual(len(node_id_hex), 64)

    def test_rtee_reflexive_patching(self):
        """Verifies that RTEE dynamically patches the canon on systemic drift."""
        engine = RTEEEngine()
        telemetry = {"systemic_drift": 0.2}
        report = engine.reconcile_policy(telemetry)
        self.assertTrue(report["updates_applied"])
        self.assertIn("REFLEXIVE-PATCH", report["new_canon_version"])

if __name__ == "__main__":
    unittest.main()
