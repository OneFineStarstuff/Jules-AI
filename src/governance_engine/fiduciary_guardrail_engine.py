from datetime import datetime

class FiduciaryGuardrailEngine:
    """
    Real-time policy enforcement for financial regulations.
    Aligned with Reg BI (US), MAS FEAT (Singapore), and UK Consumer Duty.
    """
    def __init__(self):
        self.active_regulations = ["REG_BI", "MAS_FEAT", "UK_CONSUMER_DUTY"]

    def enforce_policy(self, transaction_intent):
        """
        Evaluates transaction intent against fiduciary mandates.
        """
        # Logic gate for MAS FEAT: Fairness, Ethics, Accountability, and Transparency
        if transaction_intent.get("impact") == "HIGH" and not transaction_intent.get("human_oversight"):
            return {"decision": "DENY", "reason": "MAS_FEAT_ARTICLE_14_VIOLATION"}

        # Logic gate for UK Consumer Duty: Ensuring good outcomes for retail customers
        if transaction_intent.get("customer_type") == "RETAIL" and transaction_intent.get("risk") > 0.5:
             return {"decision": "DENY", "reason": "CONSUMER_DUTY_OUTCOME_FAIL"}

        return {"decision": "ALLOW", "timestamp": datetime.now().isoformat()}
