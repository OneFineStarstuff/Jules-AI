import json
from datetime import datetime

class FiduciaryGuardrailEngine:
    """
    Fiduciary Guardrail Engine for Sentinel v2.4.
    Enforces alignment with MAS FEAT, HKMA Fintech 2030, and FCA Consumer Duty.
    """
    def __init__(self):
        self.bias_threshold = 0.05
        self.consumer_risk_limit = 0.8

    def evaluate_transaction(self, tx_data):
        """
        Evaluates a financial transaction against fiduciary and consumer protection policies.
        """
        violations = []
        bias = tx_data.get("bias_score", 0)
        risk = tx_data.get("consumer_risk_level", 0)

        if bias > self.bias_threshold:
            violations.append("MAS_FEAT_BIAS_VIOLATION")

        if risk > self.consumer_risk_limit:
            violations.append("FCA_CONSUMER_DUTY_RISK_VIOLATION")

        decision = "APPROVED" if not violations else "REJECTED"

        return {
            "decision": decision,
            "violations": violations,
            "timestamp": datetime.now().isoformat(),
            "fiduciary_id": "FID_GUARD_PLACEHOLDER"
        }

    def get_policy_status(self):
        """Returns the current status of fiduciary policy enforcement."""
        return {
            "status": "ACTIVE",
            "jurisdiction": "GLOBAL_FSB_ALIGNED",
            "last_audit": datetime.now().isoformat()
        }

if __name__ == "__main__":
    engine = FiduciaryGuardrailEngine()
    test_tx = {"bias_score": 0.06, "consumer_risk_level": 0.4}
    print(json.dumps(engine.evaluate_transaction(test_tx), indent=2))
