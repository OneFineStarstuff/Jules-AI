import secrets
import time
import sys
import os

# Robust import handling for direct execution vs package usage
if __name__ == "__main__" and __package__ is None:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    from src.governance_engine.irmi_driver import IRMIDriver
else:
    from .irmi_driver import IRMIDriver

"""
Sovereign AGI Command Center (SACC) Orchestrator
Unifies telemetry, GDL gating, and IRMI status into an executive dashboard.
"""

class SACCOrchestrator:
    def __init__(self):
        self.systems = {
            "Credit_Nexus": {"status": "ACTIVE", "bias": 0.04, "risk": 0.2},
            "Trading_Swarm": {"status": "ACTIVE", "bias": 0.01, "risk": 0.45},
            "Citizen_Services": {"status": "ACTIVE", "bias": 0.05, "risk": 0.1}
        }
        self.hard_kill_threshold = 0.85
        self.irmi = IRMIDriver()
        self.irmi.register_interrupt()

    def get_sparkline(self, data):
        chars = " ▂▃▄▅▆▇█"
        return "".join(secrets.choice(chars) for _ in range(10))

    def render_dashboard(self):
        print("\n" + "="*60)
        print(" SOVEREIGN AGI COMMAND CENTER (SACC) v5.0")
        print(" Status: CANONICAL LOCK ACTIVE | Authority: JULES-APEX")
        print("="*60)

        for name, metrics in self.systems.items():
            spark = self.get_sparkline(None)
            status_color = "\033[92m" if metrics["status"] == "ACTIVE" else "\033[91m"
            print(f"[{status_color}{metrics['status']}\033[0m] {name.ljust(20)} | Risk: {metrics['risk']:.2f} {spark} | Bias: {metrics['bias']:.2f}")

        print("-" * 60)
        # Reflect actual IRMI lock status in the dashboard
        irmi_status = "LOCKED" if self.irmi.is_locked() else "ACTIVE"
        print(f"Global Institutional Readiness (IRMI): {irmi_status} [▆▇▇▇█]")
        print("="*60 + "\n")

    def evaluate_global_state(self):
        for name, metrics in self.systems.items():
            if metrics["risk"] > self.hard_kill_threshold:
                reason = f"T4 Violation detected in {name} (Risk: {metrics['risk']:.2f})"
                self.irmi.trigger_kill_switch(reason)
                metrics["status"] = "TERMINATED"
                return "CONTINUATION_REFUSAL_STATE"
        return "STEADY_GOVERNANCE_STATE"

if __name__ == "__main__":
    sacc = SACCOrchestrator()
    sacc.render_dashboard()
    # Simulate a sudden risk surge in Trading_Swarm
    print("Simulating risk surge in Trading_Swarm...")
    sacc.systems["Trading_Swarm"]["risk"] = 0.92
    sacc.evaluate_global_state()
    sacc.render_dashboard()
