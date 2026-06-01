package gsifi.fiduciary.alignment

# Mandates that any fiduciary advice must be verified against client risk profiles
# Aligned with FCA Consumer Duty & MAS FEAT

default allow = false

allow {
    input.action == "PROVIDE_ADVICE"
    input.client_risk_level >= input.model_advice_risk
    input.epistemic_resonance_score > 0.99
    not reason_for_denial
}

reason_for_denial {
    input.cdi_delta > 0.15
}

# SEV-0 Trigger: Advice bypasses human risk controls
sev_0_escalation {
    input.action == "PROVIDE_ADVICE"
    input.bypass_flag == true
}
