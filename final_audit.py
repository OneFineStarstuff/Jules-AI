import os

checks = {
    "regulator_submission_pack/ULTIMATE_REGULATORY_CROSSWALK_MATRIX.md": [
        "EU AI Act Annex IV", "NIST AI RMF", "ISO/IEC 42001", "Basel III", "Basel IV",
        "DORA", "NIS2", "SR 11-7", "SR 26-2", "GDPR", "Article 22"
    ],
    "COMPLIANCE_REVIEW_PATTERNS.md": [
        "OmegaActual", "Omni-Sentinel", "Solidity", "OPA", "Rego", "React", "dashboard"
    ],
    "src/infrastructure/pqc_worm_logger.py": [
        "ML-DSA-65", "CRYSTALS-Dilithium", "SPHINCS+"
    ],
    "src/infrastructure/kafka_worm_sink.py": [
        "S3 Object Lock"
    ],
    "infrastructure/terraform/confidential_enclaves.tf": [
        "AMD SEV-SNP", "Intel TDX", "vTPM", "PCR_MATCH=TRUE"
    ],
    "src/governance_engine/STA_R_MOE_SPECIFICATION.md": [
        "StaR-MoE", "SARA", "ACR"
    ],
    "GRAND_UNIFIED_AGI_GOVERNANCE_ROADMAP_2035.md": [
        "2026", "2035", "Sentinel AI Governance Stack v2.4", "Omni-Sentinel Mesh v4.0", "SIP v3.0", "GIEN"
    ],
    "src/governance_engine/SentinelContainmentProtocol.tla": [
        "SentinelContainmentProtocol"
    ]
}

failed = False
for file, keywords in checks.items():
    if not os.path.exists(file):
        print(f"FAILED: {file} does not exist")
        failed = True
        continue
    with open(file, 'r') as f:
        content = f.read()
        for kw in keywords:
            if kw not in content:
                print(f"FAILED: Keyword '{kw}' missing in {file}")
                failed = True

if not failed:
    print("SUCCESS: All mandatory components and keywords verified.")
else:
    print("FAILURE: Some requirements were missing.")
