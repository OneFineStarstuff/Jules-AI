package gsifi.systemic.risk

# Enforces Basel IV Capital Drift Index (CDI) requirements
# Trigger: RCE Drift > 15%

default allow_unbuffered = true

# Mandates capital buffer allocation
require_capital_buffer {
    input.rce_drift_score > 0.15
}

# SEV-1: Significant drift without buffer
deny_inference {
    require_capital_buffer
    input.capital_buffer_allocated == false
}

# SEV-0: Total loss of alignment
sev_0_terminal_lock {
    input.resonance_score < 0.85
    input.model_id == "tier-1-agi"
}
