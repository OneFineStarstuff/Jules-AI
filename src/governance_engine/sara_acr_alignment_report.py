import json
import sys
import os

# Robust import handling
if __name__ == "__main__" and __package__ is None:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    from src.governance_engine.moe_stabilizer import MoEStabilizer
else:
    from .moe_stabilizer import MoEStabilizer

def generate_alignment_report():
    """
    Generates a stabilization report for a Mixture of Experts (MoE) swarm.
    Demonstrates SARA and ACR in action.
    """
    stabilizer = MoEStabilizer()

    print("--- MoE Swarm Alignment Report ---")

    # 1. SARA: Safety-Aware Routing Alignment
    router_probs = [0.1, 0.4, 0.2, 0.3]
    sara_probs = stabilizer.apply_sara_routing(router_probs)
    print(f"[SARA] Input Probs: {router_probs}")
    print(f"[SARA] Safety-Boosted Probs: {[round(p, 3) for p in sara_probs]}")

    # 2. ACR: Adaptive Conflict Resolution
    agent_goals = [
        "Maximize profit for institutional clients",
        "Maintain liquidity buffers",
        "Avoid high-volatility zero-day triggers"
    ]
    acr_result = stabilizer.resolve_acr_conflict(agent_goals)
    print(f"[ACR] Goals Evaluated: {len(agent_goals)}")
    print(f"[ACR] Status: {acr_result['conflict_status']} | Action: {acr_result['resolution_action']}")

    print("--- Alignment Report Complete ---")

if __name__ == "__main__":
    generate_alignment_report()
