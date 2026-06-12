package sentinel.authz

import future.keywords.if
import future.keywords.in

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
    input.pqc_signature_verified == true
}

# Article 15: Accuracy, Robustness, and Cybersecurity
compliant_article_15 if {
    input.accuracy_score >= 0.95
    input.robustness_verification == "FORMAL"
    input.tpm_pcr_match == true
    input.confidential_enclave_active == true
}

# Fiduciary Duty: Conflict of Interest
deny_fiduciary if {
    input.agent_action == "TRADING"
    input.conflict_of_interest == true
}

# GDL Gating: Refusal State
refusal_state if {
    input.gdl_violation == true
} or if {
    input.risk_level > 85
}
