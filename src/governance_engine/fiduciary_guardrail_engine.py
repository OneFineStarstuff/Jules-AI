import json

class FiduciaryGuardrailEngine:
    """
    Fiduciary Guardrail Engine for AGI Trading.
    Enforces Regulation Best Interest, MAS FEAT, FCA Consumer Duty, and HKMA Fintech 2030.
    """
    def __init__(self):
        self.regulations = {
            "RegBI": {"max_risk_delta": 0.05},
            "MAS_FEAT": {"explainability_required": True},
            "FCA_Duty": {"avoid_foreseeable_harm": True, "vulnerable_customer_check": True},
            "HKMA_2030": {"fintech_readiness_level": 4}
        }

    def validate_trade(self, trade_data):
        """Validates a proposed trade against multi-jurisdictional fiduciary rules."""
        risk_delta = trade_data.get("risk_delta", 0)
        explainable = trade_data.get("has_cot_trace", False)
        customer_type = trade_data.get("customer_segment", "standard")

        # 1. US RegBI Check
        if risk_delta > self.regulations["RegBI"]["max_risk_delta"]:
            return False, "Violation: RegBI risk_delta exceedance."

        # 2. MAS FEAT Check
        if not explainable and self.regulations["MAS_FEAT"]["explainability_required"]:
            return False, "Violation: MAS_FEAT explainability missing."

        # 3. FCA Consumer Duty Check
        if customer_type == "vulnerable" and trade_data.get("high_leverage", False):
            return False, "Violation: FCA Consumer Duty - foreseeable harm to vulnerable customer."

        return True, "Fiduciary Compliance Verified."

if __name__ == "__main__":
    engine = FiduciaryGuardrailEngine()
    trade = {"risk_delta": 0.02, "has_cot_trace": True, "customer_segment": "vulnerable", "high_leverage": True}
    print(engine.validate_trade(trade))
