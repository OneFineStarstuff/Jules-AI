import json
import os

def verify_artifacts():
    print("Starting Pre-Commit Verification...")

    files_to_check = [
        "SENTINEL_ZERO_TRUST_ARCHITECTURE_2035.md",
        "infrastructure/terraform/confidential_enclaves.tf",
        "src/governance_engine/contracts/OmegaActual.sol",
        "src/governance_engine/contracts/OmniSentinel.sol",
        "regulator_submission_pack/oscal_gsifi_controls.json",
        "src/infrastructure/policies/compliance_rules.rego",
        "src/adaptive-ui/GovernanceDashboard.tsx",
        "src/infrastructure/zk_relayer.py",
        "src/infrastructure/hsm_integration.py",
        "SIP_V3_0_SPECIFICATION.md",
        "BBOM_PERPETUAL_ASSURANCE_PATTERN.md",
        "COMPLIANCE_REVIEW_PATTERNS.md",
        "regulator_submission_pack/RSP_V8_ULTIMATE_CONFORMITY.xml",
        "src/infrastructure/circuits/ZK_STARK_MIGRATION_GUIDE.md",
        "src/infrastructure/circuits/compliance_stark_stub.md",
        "src/governance_engine/gc_ir_bridge_spec.md",
        "src/infrastructure/gai_soc_telemetry_spec.md",
        "src/governance_engine/icgc_zk_verified_controls.md"
    ]

    success = True
    for f in files_to_check:
        if os.path.exists(f):
            print(f"[OK] Found: {f}")
        else:
            print(f"[FAIL] Missing: {f}")
            success = False

    if success:
        print("All artifacts verified.")
    return success

if __name__ == "__main__":
    if verify_artifacts():
        print("Pre-Commit Verification SUCCESSFUL.")
    else:
        exit(1)
