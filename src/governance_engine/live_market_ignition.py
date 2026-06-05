import json
from datetime import datetime

class LiveMarketIgnitionSafeguards:
    """
    Live Market Ignition Safeguards (LMIS).
    Prevents unauthorized agentic trading during high-volatility events.
    """
    def __init__(self):
        self.market_state = "STABLE"
        self.volatility_index = 0.12
        self.safeguard_status = "ENGAGED"

    def verify_ignition_safety(self, agent_intent):
        """Verifies if market conditions allow for new agentic ignition."""
        if self.volatility_index > 0.45:
            return False, "CRITICAL: Market volatility exceeds safety threshold (0.45)."

        if agent_intent.get("leverage_ratio", 0) > 10.0:
            return False, "DENIED: Excessive leverage ratio in intent vector."

        return True, "LMIS Verification Success."

if __name__ == "__main__":
    lmis = LiveMarketIgnitionSafeguards()
    intent = {"leverage_ratio": 5.0}
    print(lmis.verify_ignition_safety(intent))
