import os

keywords = [
    "2026", "2035", "Sentinel AI Governance Stack v2.4", "Omni-Sentinel Mesh v4.0",
    "Omni-Sentinel Cognitive Execution Environment", "G-Stack", "WorkflowAI Pro",
    "GAI-SOC telemetry", "zero-trust", "confidential computing", "AMD SEV-SNP",
    "Intel TDX", "vTPM", "PCR_MATCH=TRUE", "StaR-MoE", "SARA", "ACR",
    "telemetry attestation", "cryptographic telemetry integrity", "WORM",
    "ML-DSA-65", "CRYSTALS-Dilithium", "SPHINCS+", "S3 Object Lock",
    "zero-knowledge systemic risk proofs", "Basel", "SR 11-7", "SR 26-2",
    "Circom", "Groth16", "zk-STARK", "zk-SNARK", "OSCAL 1.1.2", "OPA", "Rego",
    "EU AI Act Annex IV", "NIST AI RMF", "ISO/IEC 42001", "DORA", "NIS2",
    "GDPR", "Article 22", "SentinelContainmentProtocol", "HSM", "Terraform",
    "G-SRI", "BBOM", "perpetual assurance", "GIEN", "SIP v3.0",
    "security and regulatory compliance review patterns", "OmegaActual",
    "Omni-Sentinel", "Solidity", "React", "dashboard"
]

def find_keywords():
    found = {kw: False for kw in keywords}
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'node_modules' in root or '__pycache__' in root:
            continue
        for file in files:
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for kw in keywords:
                        if kw in content:
                            found[kw] = True
            except Exception:
                continue
    return found

found_map = find_keywords()
missing = [kw for kw, found in found_map.items() if not found]

if not missing:
    print("ALL MANDATORY KEYWORDS FOUND.")
else:
    print(f"MISSING KEYWORDS: {missing}")
