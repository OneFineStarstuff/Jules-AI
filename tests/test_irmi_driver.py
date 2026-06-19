import unittest
import sys
import os

# Fix path for local execution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from src.governance_engine.irmi_driver import IRMIDriver
except ImportError:
    from src.governance_engine.irmi_driver import IRMIDriver


class TestIRMIDriver(unittest.TestCase):
    def setUp(self):
        self.driver = IRMIDriver()

    def test_initial_state(self):
        self.assertFalse(self.driver.interrupt_registered)
        self.assertFalse(self.driver.is_locked())
        self.assertEqual(len(self.driver.get_safety_logs()), 0)

    def test_register_interrupt(self):
        result = self.driver.register_interrupt()
        self.assertTrue(result)
        self.assertTrue(self.driver.interrupt_registered)
        logs = self.driver.get_safety_logs()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0]["event"], "INTERRUPT_REGISTERED")

    def test_trigger_kill_switch_success(self):
        self.driver.register_interrupt()
        result = self.driver.trigger_kill_switch("High Risk")
        self.assertTrue(result)
        self.assertTrue(self.driver.is_locked())
        logs = self.driver.get_safety_logs()
        self.assertEqual(len(logs), 2)
        self.assertEqual(logs[1]["event"], "HARDWARE_KILL_TRIGGERED")

    def test_trigger_kill_switch_without_registration(self):
        with self.assertRaises(RuntimeError):
            self.driver.trigger_kill_switch("Illegal Access")

    def test_log_integrity(self):
        self.driver.register_interrupt()
        logs = self.driver.get_safety_logs()
        self.assertIn("hash", logs[0])
        # Verifying that a simulated hash is present
        self.assertTrue(logs[0]["hash"].startswith("HASH_"))


if __name__ == "__main__":
    unittest.main()
