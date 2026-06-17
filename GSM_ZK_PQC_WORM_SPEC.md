# GSM ZK Circuit and PQC-WORM Anchoring Specification

**Apex Architect:** Jules (Principal Systems Architect & Governance Lead)
**Status:** Cryptographic Lock (v1.1.0)

---

## 1. Governance State Machine (GSM) ZK Circuit

The GSM ZK Circuit provides a succinct, non-interactive proof that a transition from `State_t` to `State_{t+1}` is valid according to the GDL Master Canon.

### 1.1 Constraint System (R1CS / PLONKY2)
*   **Input Constraints:** Verify that the Global Systemic Risk Index (G-SRI) and integrity signals used for the transition are themselves backed by signed telemetry.
*   **G-SRI Scoring Binding:** A recursive sub-circuit (or PLONKY2 recursive proof) MUST prove that the `Aggregated_Risk_Score` public input was correctly computed from the raw telemetry private inputs.
*   **Transition Invariants:**
    *   If G-SRI >= 0.85, then `State_{t+1}` MUST be `CONTINUATION_REFUSAL_STATE`.
    *   If TPM Attestation fails (PCR_MATCH=FALSE), then `State_{t+1}` MUST be `LOCKED`.
    *   Transitions to `PLANETARY_HALT` require a valid OmegaActual signature.
*   **Recursive Aggregation:** Use PLONKY2 for sub-500ms proof generation, allowing daily batches of millions of transitions to be aggregated into a single root proof.

### 1.2 Public vs. Private Inputs
*   **Public Inputs:** `Current_State`, `Target_State`, `Root_Hash_t`, `Root_Hash_{t+1}`, `Aggregated_Risk_Score`.
*   **Private Inputs:** Raw telemetry traces, individual agent SPIFFE IDs, specific GDL rule identifiers.

---

## 2. PQC-WORM Anchoring Chain

The PQC-WORM chain ensures the absolute immutability and post-quantum security of the supervisory audit trail.

### 2.1 Merkle-Based Append-Only Log
*   **Structure:** A balanced Merkle Tree where each leaf is a `Signed Decision Trace Packet`.
*   **Hashing & Domain Separation:** Adopt domain-separated hashing per **RFC 6962**:
    *   Leaves: `SHA-256(0x00 || data)`
    *   Internal Nodes: `SHA-256(0x01 || left_child || right_child)`
*   **Anchoring:** The Merkle Root (STH - Signed Tree Head) is signed using ML-DSA-87 **every 60 seconds or 1,000 entries**, whichever comes first.

### 2.2 Post-Quantum Signatures (ML-DSA-87 / Dilithium)
*   **Standard:** NIST FIPS 204.
*   **Key Management:** Keys are held in FIPS 140-3 Level 4 HSMs (Level 3 acceptable for 2026-2028 pilot phase).
*   **Quorum Signing:** Until ML-DSA threshold signing is standardized (NIST IR 8214C), a hardware-backed **k-of-n signing ceremony** is mandatory for root STH issuances.
*   **Rotation:** Mandatory 90-day hardware-backed key rotation with a signed key-rotation manifest to form a verifiable history chain.

---

## 3. Verifier Workflows

### 3.1 Institution Internal Verifier
*   Continuous background verification of leaf inclusion proofs.
*   Real-time monitoring of STH consistency across distributed S3 WORM buckets.

### 3.2 Regulator Verifier Nodes
*   Regulators run independent nodes that pull STHs and ZK-Proofs.
*   **Verification:**
    1.  Verify the ML-DSA-87 signature on the STH.
    2.  Verify the ZK-Proof against the public inputs.
    3.  Confirm that the STH represents a valid extension of the previous Merkle state (Consistency Proof).
*   **Privacy:** Regulators confirm compliance without ever accessing raw model weights or PII.

---
**Authentication:** Signed by Sovereign Authority Jules (0xDEADBEEF)
**Canonical State:** SEALED UNDER CANONICAL LOCK.
