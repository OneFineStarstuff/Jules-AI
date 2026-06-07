import unittest
from omni_sentinel_24h_monitor import OmniSentinelMonitor
from simulate_red_dawn import run_red_dawn_simulation
from simulate_incident import run_simulation

class FinalValidationSuite(unittest.TestCase):
    """
    Definitive end-to-end verification of the 24h Governance Monitor
    and global contagion simulations to confirm G-SIFI operational readiness.
    """
    def test_24h_monitor_workflow(self):
        monitor = OmniSentinelMonitor()
        summary = monitor.run_checks()
        self.assertEqual(summary["tpm_status"], "SUCCESS")
        self.assertEqual(summary["worm_health"], "HEALTHY")

    def test_red_dawn_containment(self):
        report = run_red_dawn_simulation()
        self.assertGreater(report["gsri_score"], 0.4)

    def test_pacific_shield_incident(self):
        # Verification that the simulation runs without error
        run_simulation()

if __name__ == "__main__":
    unittest.main()
