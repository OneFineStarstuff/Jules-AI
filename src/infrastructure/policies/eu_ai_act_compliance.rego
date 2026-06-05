package sentinel.authz

import future.keywords.if

default allow = false

# EU AI Act Article 14: Human Oversight Requirement
allow if {
    input.human_oversight_active == true
    input.risk_category != "UNACCEPTABLE"
    input.deception_score < 0.85
    input.gpai_systemic_risk_mitigated == true # GPAI systemic-risk provision
}

# Annex IV: Technical Documentation Compliance
compliant_annex_iv if {
    input.has_logic_explanation == true
    input.has_data_lineage == true
    input.has_hardware_attestation == true
}

# GPAI Systemic Risk Check
deny_gpai_systemic if {
    input.is_gpai == true
    input.gsri_score > 0.85
}
