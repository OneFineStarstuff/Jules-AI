import secrets
from datetime import datetime


class IRMIDriver:
    """
    Institutional Readiness Maturity Index (IRMI) Driver.
    Simulates hardware-level safety interrupts (INT 0x1A).
    """
    def __init__(self):
        self._is_locked = False
        self.interrupt_registered = False
        self.safety_logs = []

    def register_interrupt(self):
        """Registers the safety interrupt handler."""
        self.interrupt_registered = True
        self.safety_logs.append({
            "event": "INTERRUPT_REGISTERED",
            "timestamp": datetime.now().isoformat(),
            "hash": f"HASH_{secrets.token_hex(32)}"
        })
        return True

    def trigger_kill_switch(self, reason):
        """Triggers the hardware kill-switch."""
        if not self.interrupt_registered:
            raise RuntimeError("Interrupt handler not registered")

        self._is_locked = True
        self.safety_logs.append({
            "event": "HARDWARE_KILL_TRIGGERED",
            "reason": reason,
            "timestamp": datetime.now().isoformat(),
            "hash": f"HASH_{secrets.token_hex(32)}"
        })
        return True

    def is_locked(self):
        """Returns the current lock status."""
        return self._is_locked

    def get_safety_logs(self):
        """Returns the internal safety logs."""
        return self.safety_logs


if __name__ == "__main__":
    driver = IRMIDriver()
    driver.register_interrupt()
