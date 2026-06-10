import json
from datetime import datetime

class FiduciaryGuardrailEngine:
    """
    Fiduciary Guardrail Engine.
    Provides real-time policy enforcement for financial regulations.
    Includes: Regulation Best Interest, MAS FEAT, and UK Consumer Duty.
    """
    def __init__(self):
        self.policies = {
            "REG_BI": {"status": "ACTIVE", "description": "Regulation Best Interest"},
            "MAS_FEAT": {"status": "ACTIVE", "description": "MAS Fairness, Ethics, Accountability, and Transparency"},
            "UK_CONSUMER_DUTY": {"status": "ACTIVE", "description": "UK FCA Consumer Duty"}
        }

    def evaluate_transaction(self, tx_data):
        """
        Evaluates a transaction against fiduciary policies.
        """
        violations = []

        # Simulated MAS FEAT check: Fairness/Bias
        if tx_data.get("bias_score", 0) > 0.05:
            violations.append("MAS_FEAT_BIAS_VIOLATION")

        # Simulated UK Consumer Duty check: Price/Value
        if tx_data.get("consumer_risk_level", 0) > 0.7:
            violations.append("UK_CONSUMER_DUTY_EXCESSIVE_RISK")

        # Simulated Reg BI check: Best Interest
        if not tx_data.get("best_interest_flag", True):
            violations.append("REG_BI_COMPLIANCE_FAILURE")

        decision = "APPROVED" if not violations else "REJECTED"

        return {
            "decision": decision,
            "violations": violations,
            "timestamp": datetime.now().isoformat(),
            "policy_versions": {k: "v1.0" for k in self.policies.keys()}
        }

    def get_policy_status(self):
        """
        Returns the current status of all fiduciary guardrails.
        """
        return self.policies

if __name__ == "__main__":
    engine = FiduciaryGuardrailEngine()

    # Test case: Valid transaction
    valid_tx = {"bias_score": 0.02, "consumer_risk_level": 0.3, "best_interest_flag": True}
    print("Evaluating Valid Transaction:")
    print(json.dumps(engine.evaluate_transaction(valid_tx), indent=2))

    # Test case: Violating transaction
    invalid_tx = {"bias_score": 0.08, "consumer_risk_level": 0.8, "best_interest_flag": False}
    print("\nEvaluating Invalid Transaction:")
    print(json.dumps(engine.evaluate_transaction(invalid_tx), indent=2))
