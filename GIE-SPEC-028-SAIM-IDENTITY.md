# GIE-SPEC-028: Sovereign Authority Identity Management (SAIM)
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Hierarchy of Trust
The **SAIM** defines the cryptographic identity structures for the Omni-Sentinel governance mesh.

### 1.1 Root: Sovereign Authority (Jules-Apex)
- **Role:** Final arbiter of the GDL Master Canon and Global ROI.
- **Identity:** Multi-signature threshold key (3-of-5) distributed across globally diverse cold-storage HSMs.
- **Capability:** Issues the Global-GACMO and Sentinel-Safety-Kernel keys.

### 1.2 Tier 2: Institutional GIE-CA
- **Role:** Issues institutional ZK-certificates and manages regional GIEN registration.
- **Identity:** X.509 SVID signed by the Sovereign Root.

### 1.3 Tier 3: Reasoning Enclaves
- **Role:** Autonomous inference and policy enforcement.
- **Identity:** Hardware-bound SVIDs anchored in node-level TPMs.

## 2. Identity Life-cycle
- **Enrollment:** Mandatory vTPM remote attestation and institutional vetting.
- **Rotation:** Automated SVID rotation every 24 hours via SPIFFE/Spire.
- **Revocation:** Sub-100ms global revocation broadcast via the GIEN Alpha Path upon equivocation detection.

## 3. Cryptographic Standards
- **Signatures:** ML-DSA-87 (CRYSTALS-Dilithium) for all persistent anchors.
- **Encryption:** ML-KEM-1024 (Kyber) for cross-enclave session key exchange.
