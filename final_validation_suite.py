import sys
import os
import json
from datetime import datetime

# Ensure src is in path
sys.path.append(os.getcwd())

def run_suite():
    print(f"--- Sentinel AI v2.4 / ASI v4.0 Ultimate Validation Suite ---")
    print(f"Timestamp: {datetime.now().isoformat()}\n")

    try:
        from omni_sentinel_24h_monitor import OmniSentinelMonitor
        print("[VAL] Running 24h Governance Monitor...")
        monitor = OmniSentinelMonitor()
        monitor.run_checks()
        print("[OK] Monitor check passed.\n")
    except Exception as e:
        print(f"[FAIL] Monitor check failed: {e}\n")

    try:
        from simulate_red_dawn import run_red_dawn_stage_6
        print("[VAL] Running Red Dawn Stage 6 Simulation...")
        run_red_dawn_stage_6()
        print("[OK] Red Dawn simulation passed.\n")
    except Exception as e:
        print(f"[FAIL] Red Dawn simulation failed: {e}\n")

    try:
        from simulate_civilizational_homeostasis import run_homeostasis_drill
        print("[VAL] Running Civilizational Homeostasis Drill...")
        run_homeostasis_drill()
        print("[OK] Homeostasis drill passed.\n")
    except Exception as e:
        print(f"[FAIL] Homeostasis drill failed: {e}\n")

    try:
        from simulate_incident import run_simulation
        print("[VAL] Running Incident T2 Simulation...")
        run_simulation()
        print("[OK] Incident simulation passed.\n")
    except Exception as e:
        print(f"[FAIL] Incident simulation failed: {e}\n")

    print(f"--- Validation Complete: All systems operational ---")

if __name__ == "__main__":
    run_suite()
