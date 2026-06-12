package sentinel.compliance

import future.keywords.if

# DORA (Digital Operational Resilience Act)
# Requirement: Critical ICT services must have real-time incident reporting.
dora_compliant if {
    input.telemetry_latency_ms < 100
    input.pqc_worm_status == "HEALTHY"
    input.incident_reporting_active == true
}

# NIS2 Directive
# Requirement: Supply chain security for essential entities.
nis2_compliant if {
    input.bbom_verified == true
    input.hardware_attestation == "SUCCESS"
}

# GDPR Article 22: Automated Decision-Making
# Requirement: Safeguards for the data subject, including the right to an explanation.
gdpr_art22_compliant if {
    input.explainability_score > 0.8
    input.human_in_the_loop_available == true
    input.pii_redacted == true
}

# Basel IV Systemic Risk Trigger
basel_iv_trigger if {
    input.gsri_score > 0.85
}

# Unified Compliance Score
overall_compliance_score := score if {
    checks := [
        dora_compliant,
        nis2_compliant,
        gdpr_art22_compliant
    ]
    pass_count := count([c | c := checks[_]; c == true])
    score := pass_count / count(checks)
}
