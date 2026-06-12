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
        "src/adaptive-ui/GovernanceDashboard.tsx"
    ]

    for f in files_to_check:
        if os.path.exists(f):
            print(f"[OK] Found: {f}")
        else:
            print(f"[FAIL] Missing: {f}")
            return False

    print("Artifact existence verified.")
    return True

if __name__ == "__main__":
    if verify_artifacts():
        print("Pre-Commit Verification SUCCESSFUL.")
    else:
        exit(1)
