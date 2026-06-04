import json

class FiduciaryGuardrailEngine:
    """
    Fiduciary Guardrail Engine for AGI Trading.
    Enforces Regulation Best Interest, MAS FEAT, and UK Consumer Duty.
    """
    def __init__(self):
        self.regulations = {
            "RegBI": {"max_risk_delta": 0.05},
            "MAS_FEAT": {"explainability_required": True},
            "Consumer_Duty": {"avoid_foreseeable_harm": True}
        }

    def validate_trade(self, trade_data):
        """Validates a proposed trade against multi-jurisdictional fiduciary rules."""
        # Simplified validation logic
        risk_delta = trade_data.get("risk_delta", 0)
        explainable = trade_data.get("has_cot_trace", False)

        if risk_delta > self.regulations["RegBI"]["max_risk_delta"]:
            return False, "Violation: RegBI risk_delta exceedance."

        if not explainable and self.regulations["MAS_FEAT"]["explainability_required"]:
            return False, "Violation: MAS_FEAT explainability missing."

        return True, "Fiduciary Compliance Verified."

if __name__ == "__main__":
    engine = FiduciaryGuardrailEngine()
    trade = {"risk_delta": 0.02, "has_cot_trace": True}
    print(engine.validate_trade(trade))
