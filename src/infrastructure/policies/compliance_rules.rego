package sentinel.compliance

import future.keywords.if

# DORA (Digital Operational Resilience Act)
dora_compliant if {
    input.telemetry_latency_ms < 100
    input.pqc_worm_status == "HEALTHY"
    input.incident_reporting_active == true
}

# NIS2 Directive
nis2_compliant if {
    input.bbom_verified == true
    input.hardware_attestation == "SUCCESS"
}

# ISO/IEC 42001: AI Management System
iso42001_compliant if {
    input.registry_status == "SYNCHRONIZED"
    input.lifecycle_audit_passed == true
}

# SR 11-7: Model Risk Management
sr11_7_compliant if {
    input.validation_variance < 0.02
    input.independent_review_active == true
}

# GDPR Article 22
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
        iso42001_compliant,
        sr11_7_compliant,
        gdpr_art22_compliant
    ]
    pass_count := count([c | c := checks[_]; c == true])
    score := pass_count / count(checks)
}
