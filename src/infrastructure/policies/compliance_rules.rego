package sentinel.compliance

import future.keywords.if

# DORA (Digital Operational Resilience Act)
# Mapping: Article 14 (ICT Risk Management)
dora_compliant if {
    input.telemetry_latency_ms < 100
    input.pqc_worm_status == "HEALTHY"
    input.incident_reporting_active == true
}

# NIS2 Directive
# Mapping: Supply Chain & Cryptographic Hygiene
nis2_compliant if {
    input.bbom_verified == true
    input.hardware_attestation == "SUCCESS"
    input.pqc_mode == "MULTI_ALGO_VERIFIED"
}

# ISO/IEC 42001: AI Management System
# Mapping: A.5.2 (AI System Lifecycle)
iso42001_compliant if {
    input.registry_status == "SYNCHRONIZED"
    input.lifecycle_audit_passed == true
    input.gdl_master_canon_hash != ""
}

# SR 11-7: Model Risk Management
# Mapping: Continuous Validation & Effective Challenge
sr11_7_compliant if {
    input.validation_variance < 0.02
    input.independent_review_active == true
}

# SR 26-2: Operational Resilience & Agent Audit
# Mapping: Auditability of Autonomous Systems
sr26_2_compliant if {
    input.audit_trail_immutable == true
    input.non_repudiation_confirmed == true
}

# GDPR Article 22: Automated Decision-Making
# Mapping: Safeguards & Right to Explanation
gdpr_art22_compliant if {
    input.explainability_score > 0.8
    input.human_in_the_loop_available == true
    input.pii_redacted == true
}

# Basel IV Systemic Risk Trigger
# Mapping: Operational Risk Capital Surcharge
basel_iv_trigger if {
    input.gsri_score > 0.85
}

# EU AI Act Annex IV
# Mapping: Technical Documentation for High-Risk AI
eu_ai_act_annex_iv_compliant if {
    input.has_logic_explanation == true
    input.has_data_lineage == true
    input.has_hardware_attestation == true
}

# Unified Compliance Score
overall_compliance_score := score if {
    checks := [
        dora_compliant,
        nis2_compliant,
        iso42001_compliant,
        sr11_7_compliant,
        sr26_2_compliant,
        gdpr_art22_compliant,
        eu_ai_act_annex_iv_compliant
    ]
    pass_count := count([c | c := checks[_]; c == true])
    score := pass_count / count(checks)
}
