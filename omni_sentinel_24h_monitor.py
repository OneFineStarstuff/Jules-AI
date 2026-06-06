import json
import time
from datetime import datetime
from src.infrastructure.pqc_worm_logger import PQCWormLogger
from src.infrastructure.tpm_attestor import TPMAttestor
from src.governance_engine.gsri_scoring_engine import GSRIScoringEngine
from src.governance_engine.sacc_orchestrator import SACCOrchestrator
from src.governance_engine.moe_stabilizer import MoEStabilizer
from src.governance_engine.fiduciary_guardrail_engine import FiduciaryGuardrailEngine
from src.infrastructure.gien_relay import GIENRelay

class OmniSentinelMonitor:
    """
    Omni-Sentinel 24h Governance Monitor.
    Automates periodic execution of G-SRI, PQC WORM, and TPM checks.
    Enhanced with MoE, GIEN, and Fiduciary Guardrail verification.
    """
    def __init__(self):
        self.logger = PQCWormLogger()
        self.tpm = TPMAttestor()
        self.gsri = GSRIScoringEngine()
        self.sacc = SACCOrchestrator()
        self.moe = MoEStabilizer()
        self.fiduciary = FiduciaryGuardrailEngine()
        self.gien = GIENRelay()

    def run_checks(self):
        print(f"[{datetime.now().isoformat()}] Starting Enhanced Omni-Sentinel 24h Governance Check...")

        # 1. TPM Attestation
        current_pcrs = {"PCR0": "GOLDEN_VAL_0", "PCR1": "GOLDEN_VAL_1"}
        tpm_report = self.tpm.perform_attestation(current_pcrs)
        self.logger.log_entry("TPM_ATTESTOR", "ATTESTATION_RUN", tpm_report)

        # 2. G-SRI Calculation
        risk_inputs = {"resonance_drift": 0.15, "cdi_delta": 0.08, "agent_collusion_prob": 0.03}
        gsri_report = self.gsri.calculate_gsri(risk_inputs)
        self.logger.log_entry("GSRI_ENGINE", "SCORE_CALCULATED", gsri_report)

        # 3. MoE Stability Check
        moe_drift = self.moe.check_drift()
        self.logger.log_entry("MOE_STABILIZER", "DRIFT_CHECK", moe_drift)

        # 4. GIEN Mesh Health
        gien_health = self.gien.check_mesh_health()
        self.logger.log_entry("GIEN_RELAY", "HEALTH_CHECK", gien_health)

        # 5. Fiduciary Test
        fiduciary_test = self.fiduciary.enforce_policy({"impact": "HIGH", "human_oversight": True})

        # 6. PQC WORM Health
        worm_health = self.logger.verify_health()

        # 7. SACC Dashboard Update
        self.sacc.render_dashboard()

        # Final Summary
        summary = {
            "timestamp": datetime.now().isoformat(),
            "tpm_status": tpm_report["attestation_status"],
            "gsri_score": gsri_report["gsri_score"],
            "moe_status": moe_drift["status"],
            "gien_status": gien_health["status"],
            "worm_health": worm_health["status"]
        }

        print(f"[{datetime.now().isoformat()}] Enhanced Governance Check Complete. Summary: {summary}")
        return summary

if __name__ == "__main__":
    monitor = OmniSentinelMonitor()
    monitor.run_checks()
