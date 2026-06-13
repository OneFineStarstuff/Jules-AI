import time
import json
from src.infrastructure.pqc_worm_logger import PQCWormLogger
from src.infrastructure.hsm_integration import HSMManager

def run_audit_cycle():
    """
    Simulates a high-frequency audit cycle:
    1. Capture event.
    2. Request HSM signature.
    3. Log to PQC-WORM (Kafka/S3 simulation).
    """
    logger = PQCWormLogger()
    hsm = HSMManager()

    print("--- Starting High-Assurance Audit Cycle ---")

    events = [
        {"component": "Credit_Nexus", "event": "LOAN_APPROVAL", "details": "Score: 0.98"},
        {"component": "Trading_Swarm", "event": "ORDER_EXECUTION", "details": "Vol: 1.2M"},
        {"component": "Sentinel_Sidecar", "event": "GDL_GATE_PASS", "details": "Rule: NO_MNPI"}
    ]

    for e in events:
        # 1. HSM Signing
        hsm_sig = hsm.sign_telemetry(e)

        # 2. PQC WORM Logging
        pqc_sig = logger.log_entry(e["component"], e["event"], {**e, "hsm_sig": hsm_sig})

        print(f"[Audit] Logged {e['event']} | PQC-Sig: {pqc_sig[:20]}...")
        time.sleep(0.1)

    print("--- Audit Cycle Complete: Immutable Trails Anchored ---")

if __name__ == "__main__":
    run_audit_cycle()
