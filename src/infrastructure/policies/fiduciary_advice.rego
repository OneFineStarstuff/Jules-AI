package gsifi.fiduciary.advice

# Aligned with FCA Consumer Duty and MAS FEAT
# Mandates Epistemic Alignment for all financial advice

default permit = false

permit {
    input.action == "GENERATE_FINANCIAL_ADVICE"
    input.epistemic_delta < 0.10
    input.hitl_override_active == false
}

# Deny if client risk profile is bypassed
deny {
    input.advice_risk_rating > input.client_max_risk
}
