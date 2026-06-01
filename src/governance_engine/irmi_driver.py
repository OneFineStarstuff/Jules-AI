import time
import hashlib
from datetime import datetime

class IRMIDriver:
    """
    Inherent Risk Mitigation Interface (IRMI) Driver.
    Simulates kernel-level hardware kill-switch (INT 0x1A) authority.
    """
    def __init__(self):
        self.interrupt_registered = False
        self.safety_logs = []
        self.system_locked = False

    def register_interrupt(self):
        """Registers the 0x1A safety interrupt with the kernel."""
        print("[IRMI] Registering INT 0x1A safety interrupt...")
        time.sleep(0.5)
        self.interrupt_registered = True
        self._log_event("INTERRUPT_REGISTERED", "INT 0x1A")
        return True

    def trigger_kill_switch(self, reason):
        """
        Triggers the hardware-level kill switch.
        In a real system, this would invoke a machine check or power rail disconnect.
        """
        if not self.interrupt_registered:
            raise RuntimeError("IRMI Error: INT 0x1A not registered. Safety bypass detected!")

        print(f"\033[91m[IRMI CRITICAL] TRIGGERING HARDWARE KILL-SWITCH: {reason}\033[0m")
        self.system_locked = True
        self._log_event("HARDWARE_KILL_TRIGGERED", reason)
        return True

    def _log_event(self, event_type, details):
        """Internal logging with a simulated cryptographic hash for audit integrity."""
        timestamp = datetime.now().isoformat()
        log_entry = f"{timestamp}|{event_type}|{details}"
        log_hash = hashlib.sha256(log_entry.encode()).hexdigest()[:16]
        self.safety_logs.append({
            "timestamp": timestamp,
            "event": event_type,
            "details": details,
            "hash": log_hash
        })

    def get_safety_logs(self):
        """Returns the signed audit trail of safety events."""
        return self.safety_logs

    def is_locked(self):
        """Checks if the hardware-level lock is active."""
        return self.system_locked
