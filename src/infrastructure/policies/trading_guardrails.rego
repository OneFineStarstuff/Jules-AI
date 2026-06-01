package gsifi.trading.guardrails

# Enforces hard limits on autonomous trading agents
# Aligned with Basel IV & SR 11-7

default allow = false

allow {
    input.trade_amount <= input.limit_max
    input.volatility_index < 0.4
    input.cas_spp_proof_verified == true
}

# Sanction: Immediate trade suspension if systemic drift detected
suspend_trading {
    input.systemic_stability_score < 0.85
}

# SEV-0: Unauthorized circuit bypass
sev_0_escalation {
    input.kernel_boundary_breach == true
}
