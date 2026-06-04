package sentinel.authz

import future.keywords.if

default allow = false

# EU AI Act Article 14: Human Oversight Requirement
allow if {
    input.human_oversight_active == true
    input.risk_category != "UNACCEPTABLE"
    input.deception_score < 0.85
}

# Annex IV: Technical Documentation Compliance
compliant_annex_iv if {
    input.has_logic_explanation == true
    input.has_data_lineage == true
    input.has_hardware_attestation == true
}
