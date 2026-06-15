import os
import subprocess

requirements = [
    ("GRAND_UNIFIED_AGI_GOVERNANCE_ROADMAP_2035.md", ["2026-2035", "Decadal", "Sentinel AI Governance Stack v2.4", "Omni-Sentinel Mesh v4.0", "SIP v3.0", "GIEN"]),
    ("G_STACK_TECHNICAL_SPEC.md", ["G-Stack", "WorkflowAI Pro", "GAI-SOC telemetry", "Cognitive Execution Environment", "zero-trust", "telemetry attestation"]),
    ("infrastructure/terraform/confidential_enclaves.tf", ["AMD SEV-SNP", "Intel TDX", "PCR_MATCH=TRUE", "vTPM"]),
    ("src/governance_engine/STA_R_MOE_SPECIFICATION.md", ["StaR-MoE", "routing stabilization", "SARA", "ACR"]),
    ("src/infrastructure/pqc_worm_logger.py", ["ML-DSA-65", "CRYSTALS-Dilithium", "SPHINCS+"]),
    ("src/infrastructure/kafka_worm_sink.py", ["S3 Object Lock"]),
    ("src/infrastructure/zk_systemic_risk_proof.py", ["Basel III", "Basel IV", "SR 11-7", "SR 26-2", "Circom", "Groth16"]),
    ("ZK_STARK_MIGRATION_GUIDE.md", ["zk-STARK"]),
    ("src/infrastructure/zk_relayer.py", ["zk-SNARK", "relayer pipeline"]),
    ("regulator_submission_pack/ULTIMATE_REGULATORY_CROSSWALK_MATRIX.md", ["EU AI Act Annex IV", "NIST AI RMF", "ISO/IEC 42001", "DORA", "NIS2", "GDPR", "Article 22"]),
    ("src/governance_engine/SentinelContainmentProtocol.tla", ["SentinelContainmentProtocol", "invariants"]),
    ("src/infrastructure/hsm_integration.py", ["HSM"]),
    ("G_SRI_TECHNICAL_WHITE_PAPER.md", ["G-SRI"]),
    ("BBOM_PERPETUAL_ASSURANCE_PATTERN.md", ["BBOM", "perpetual assurance"]),
    ("COMPLIANCE_REVIEW_PATTERNS.md", ["OmegaActual", "Omni-Sentinel", "Solidity", "OPA", "Rego", "React", "dashboard"])
]

all_passed = True
for filepath, keywords in requirements:
    if not os.path.exists(filepath):
        print(f"MISSING FILE: {filepath}")
        all_passed = False
        continue

    with open(filepath, 'r') as f:
        content = f.read()
        for kw in keywords:
            if kw not in content:
                print(f"MISSING KEYWORD '{kw}' in {filepath}")
                all_passed = False

if all_passed:
    print("ALL VERIFICATION KEYWORDS FOUND.")
else:
    print("SOME VERIFICATIONS FAILED.")
