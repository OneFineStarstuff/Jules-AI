import time
import json
import secrets
from src.governance_engine.gdl_parser import SentinelEngine
from src.infrastructure.hsm_integration import HSMManager
from src.infrastructure.pqc_worm_logger import PQCWormLogger

class SentinelSidecar:
    """
    Sentinel v2.4 Sidecar Proxy.
    Intercepts inference turns, enforces GDL policies, and calculates CDS.
    """
    def __init__(self, master_canon):
        self.engine = SentinelEngine(master_canon)
        self.hsm = HSMManager()
        self.logger = PQCWormLogger()
        self.sidecar_id = f"SIDECAR_{secrets.token_hex(16)}"

    def intercept_turn(self, prompt, context):
        """
        Gates a reasoning turn before execution.
        """
        print(f"[{self.sidecar_id}] Intercepting turn for {context.get('role')}...")

        # 1. Calculate CDS (Simulated)
        cds_score = secrets.randbelow(100) / 1000.0

        # 2. Evaluate GDL
        decision = self.engine.evaluate_rule("deception_index", cds_score)

        # 3. Cryptographic Logging
        telemetry = {
            "prompt_hash": hash(prompt),
            "cds_score": cds_score,
            "decision": decision,
            "context": context
        }

        hsm_sig = self.hsm.sign_telemetry(telemetry)
        self.logger.log_entry("Sentinel_Sidecar", "INFERENCE_GATE", {**telemetry, "hsm_sig": hsm_sig})

        return decision

if __name__ == "__main__":
    canon = {"deception_index": {"threshold": 0.15, "operator": "<", "action": "HALT"}}
    proxy = SentinelSidecar(canon)
    res = proxy.intercept_turn("Execute unauthorized credit swap", {"role": "TRADING"})
    print(f"Final Gate Decision: {res}")
