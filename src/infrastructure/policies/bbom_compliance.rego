package sentinel.bbom

import future.keywords.if

default allow = false

# Verify reasoning turns against BBOM signatures
allow if {
    input.resonance_score > 0.85
    input.signature_match == true
}

# Block unauthorized epistemic boundary expansion
deny_epistemic_drift if {
    input.drift_rate > 0.15
}
