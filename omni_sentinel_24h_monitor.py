import json
import time
from datetime import datetime
from src.infrastructure.pqc_worm_logger import PQCWormLogger
from src.infrastructure.tpm_attestor import TPMAttestor
from src.governance_engine.gsri_scoring_engine import GSRIScoringEngine
from src.governance_engine.sacc_orchestrator import SACCOrchestrator

class OmniSentinelMonitor:
    """
    Omni-Sentinel 24h Governance Monitor.
    Automates periodic execution of G-SRI, PQC WORM, and TPM checks.
    """
    def __init__(self):
        self.logger = PQCWormLogger()
        self.tpm = TPMAttestor()
        self.gsri = GSRIScoringEngine()
        self.sacc = SACCOrchestrator()
        self.log_file = "monitor_sim.log"

    def run_checks(self):
        print(f"[{datetime.now().isoformat()}] Starting Omni-Sentinel 24h Governance Check...")

        # 1. TPM Attestation with placeholders
        current_pcrs = {
            "PCR0": "GOLDEN_VAL_0",
            "PCR1": "GOLDEN_VAL_1"
        }
        tpm_report = self.tpm.perform_attestation(current_pcrs)
        self.logger.log_entry("TPM_ATTESTOR", "ATTESTATION_RUN", tpm_report)

        # 2. G-SRI Calculation
        risk_inputs = {
            "resonance_drift": 0.15,
            "cdi_delta": 0.08,
            "agent_collusion_prob": 0.03
        }
        gsri_report = self.gsri.calculate_gsri(risk_inputs)
        self.logger.log_entry("GSRI_ENGINE", "SCORE_CALCULATED", gsri_report)

        # 3. PQC WORM Health
        worm_health = self.logger.verify_health()

        # 4. SACC Dashboard Update
        self.sacc.render_dashboard()

        # Final Summary
        summary = {
            "timestamp": datetime.now().isoformat(),
            "tpm_status": tpm_report["attestation_status"],
            "gsri_score": gsri_report["gsri_score"],
            "gsri_status": gsri_report["status"],
            "worm_health": worm_health["status"]
        }

        print(f"[{datetime.now().isoformat()}] Governance Check Complete. Summary: {summary}")
        return summary

if __name__ == "__main__":
    monitor = OmniSentinelMonitor()
    monitor.run_checks()
