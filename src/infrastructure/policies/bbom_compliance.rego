package gsifi.bbom.compliance

# Enforces that all AGI turns must be verified against their Behavioral Bill of Materials
# Aligned with EU AI Act Art 11 & SR 11-7

default allow_execution = false

allow_execution {
    input.bbom_signature_valid == true
    input.behavioral_invariant_breach == false
    input.cas_spp_proof_generated == true
    not high_severity_drift
}

# SEV-1: Behavioral Drift Detected
high_severity_drift {
    input.resonance_score < 0.95
}

# SEV-0: Unauthorized register modification
terminal_lock {
    input.action == "MODIFY_KERNEL_REGISTER"
    input.auth_zk_proof_valid == false
}
