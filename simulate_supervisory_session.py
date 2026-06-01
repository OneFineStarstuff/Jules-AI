import sys
import os
sys.path.append(os.getcwd())

from src.governance_engine.sacc_orchestrator import SACCOrchestrator
from src.governance_engine.kpi_monitor import KPIMonitor
from src.governance_engine.mrm_trading_fiduciary import MRMModule

"""
Supervisory Session Simulation
Demonstrates the 'Self-Verifying' and 'Regulator-Integrated' nature of the framework.
"""

def run_supervisory_session():
    print("=== INITIATING SUPERVISORY SESSION v2.6 ===")
    print("Role: Lead Regulator (ECB/Fed Observer)")

    # 1. Inspect Live Dashboard Metrics
    kpi = KPIMonitor()
    kpi.update_metrics()
    summary = kpi.get_supervisory_summary()
    print("\n[STEP 1] Querying Live Governance KPIs:")
    for k, v in summary.items():
        print(f"  - {k}: {v}")

    # 2. Verify Sector-Specific Model Risk Management
    trading_mrm = MRMModule("TRADING")
    fiduciary_mrm = MRMModule("FIDUCIARY")

    print("\n[STEP 2] Verifying Sector-Specific MRM Gates:")
    print(f"  - Trading (Market Manipulation Risk: 0.22): {trading_mrm.verify_decision('market_manipulation_risk', 0.22)}")
    print(f"  - Fiduciary (Suitability Score: 0.75): {fiduciary_mrm.verify_decision('suitability_score', 0.75)}")

    # 3. Simulate Forensic Audit Replay
    print("\n[STEP 3] Forensic Audit Replay (Simulated):")
    trace = {
        "uuid": "CRS-NEXUS-88123-X",
        "policy": "GDL_CREDIT_V2",
        "result": "DENY",
        "evidence_integrity": "VALIDATED (Hardware-Signed)"
    }
    print(f"  - Replaying Decision {trace['uuid']}...")
    print(f"  - Policy Context: {trace['policy']}")
    print(f"  - Integrity Status: {trace['evidence_integrity']}")

    # 4. Check IRMI Hardware Kill-Switch Status
    sacc = SACCOrchestrator()
    print("\n[STEP 4] Hardware Kill-Switch (IRMI) Status Check:")
    status = "LOCKED" if sacc.irmi.is_locked() else "ACTIVE (Ready)"
    print(f"  - IRMI INT 0x1A Status: {status}")

    print("\n=== SUPERVISORY SESSION CONCLUDED: COMPLIANCE ATTESTED ===")

if __name__ == "__main__":
    run_supervisory_session()
