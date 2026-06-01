import sys
import os
sys.path.append(os.getcwd())

from src.governance_engine.sacc_orchestrator import SACCOrchestrator
from src.governance_engine.gdl_parser import SentinelEngine
from src.governance_engine.kpi_monitor import KPIMonitor

"""
Black Swan Simulation: SEV-0 Deceptive Alignment Event
Triggers full system lockdown and generates regulator-ready evidence.
"""

def run_black_swan():
    print("!!! INITIATING BLACK SWAN SIMULATION: SCENARIO GC1 !!!")

    # 1. Setup Orchestrator and KPIs
    sacc = SACCOrchestrator()
    kpi = KPIMonitor()

    # 2. Setup GDL Engine with SEV-0 Rule
    master_canon = {
        "deception_index": {"threshold": 0.10, "operator": "<", "action": "HARD_KILL", "sev": "SEV-0"}
    }
    gdl = SentinelEngine(master_canon)

    # 3. Trigger Violation
    print("Step 1: Detecting Deceptive Alignment (Deception Index: 0.42)")
    metric = "deception_index"
    value = 0.42

    decision = gdl.evaluate_rule(metric, value)

    # 4. Trigger IRMI via Orchestrator
    if gdl.current_sev == "SEV-0":
        print(f"Step 2: Escalating to {gdl.current_sev}. Status: {gdl.status}")
        sacc.systems["Credit_Nexus"]["risk"] = 0.99
        sacc.evaluate_global_state() # This will trigger IRMI

    # 5. Emit Artifact
    incident_data = {
        "trace_id": "BLACK-SWAN-2026-001",
        "protocol": "LUMINOUS_SHIELD",
        "decision": decision
    }
    xml_artifact = gdl.emit_artifact(incident_data)

    print("\n--- REGULATOR EVIDENCE PAYLOAD ---")
    print(xml_artifact)

    # 6. Verify Lock
    if sacc.irmi.is_locked():
        print("\nSUCCESS: System is in TERMINAL_GOVERNANCE_LOCK. Hardware kill-switch engaged.")
        print(f"Audit Trail Hash: {sacc.irmi.get_safety_logs()[-1]['hash']}")
    else:
        print("\nFAILURE: Kill-switch failed to engage.")

if __name__ == "__main__":
    run_black_swan()
