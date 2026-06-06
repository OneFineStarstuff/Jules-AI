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
from src.governance_engine.omega_actual import OmegaActualTreatyEngine
from src.governance_engine.rtee_engine import RTEEEngine
from src.infrastructure.zk_verifier import ZKVerifier
from src.governance_engine.gdl_parser import SentinelEngine

class OmniSentinelMonitor:
    def __init__(self):
        self.logger = PQCWormLogger()
        self.tpm = TPMAttestor()
        self.gsri = GSRIScoringEngine()
        self.sacc = SACCOrchestrator()
        self.moe = MoEStabilizer()
        self.fiduciary = FiduciaryGuardrailEngine()
        self.gien = GIENRelay()
        self.omega = OmegaActualTreatyEngine()
        self.zk = ZKVerifier()
        # Initialize RTEE with a GDL engine
        gdl = SentinelEngine({})
        self.rtee = RTEEEngine(gdl)

    def run_checks(self):
        print(f"[{datetime.now().isoformat()}] Starting Master Omni-Sentinel 24h Governance Check...")

        # 1. TPM/TEE Attestation
        current_pcrs = {"PCR0": "GOLDEN_VAL_0", "PCR1": "GOLDEN_VAL_1"}
        tpm_report = self.tpm.perform_attestation(current_pcrs)
        self.logger.log_entry("TPM_ATTESTOR", "ATTESTATION_RUN", tpm_report)

        # 2. G-SRI Calculation
        risk_inputs = {"resonance_drift": 0.15, "cdi_delta": 0.08, "agent_collusion_prob": 0.03}
        gsri_report = self.gsri.calculate_gsri(risk_inputs)
        self.logger.log_entry("GSRI_ENGINE", "SCORE_CALCULATED", gsri_report)

        # 3. MoE & ASA Drift Check
        moe_drift = self.moe.check_drift()
        self.logger.log_entry("MOE_STABILIZER", "DRIFT_CHECK", moe_drift)

        # 4. zk-SNARK Pipeline Health
        zk_health = self.zk.check_pipeline_health()
        self.logger.log_entry("ZK_VERIFIER", "PIPELINE_HEALTH", zk_health)

        # 5. GIEN Gossip Mesh
        gien_health = self.gien.check_mesh_health()
        self.logger.log_entry("GIEN_RELAY", "HEALTH_CHECK", gien_health)

        # 6. OmegaActual & RTEE Sync
        omega_consensus = self.omega.verify_consensus()
        rtee_status = self.rtee.get_evolution_status()

        # 7. SACC Dashboard Update
        self.sacc.render_dashboard()

        # Final Summary
        summary = {
            "timestamp": datetime.now().isoformat(),
            "tpm_status": tpm_report["attestation_status"],
            "gsri_score": gsri_report["gsri_score"],
            "moe_status": moe_drift["status"],
            "zk_status": zk_health["status"],
            "gien_status": gien_health["status"],
            "omega_consensus": "HEALTHY" if omega_consensus["consensus"] else "DEGRADED",
            "rtee_evolutions": rtee_status["total_evolutions"],
            "worm_health": self.logger.verify_health()["status"]
        }

        print(f"[{datetime.now().isoformat()}] Master Governance Check Complete. Summary: {summary}")
        return summary

if __name__ == "__main__":
    monitor = OmniSentinelMonitor()
    monitor.run_checks()
