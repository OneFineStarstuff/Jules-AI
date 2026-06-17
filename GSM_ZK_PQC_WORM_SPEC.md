# GSM ZK Circuit and PQC-WORM Anchoring Specification

**Apex Architect:** Jules (Principal Systems Architect & Governance Lead)
**Status:** Cryptographic Lock (v1.1.1)

---

## 1. Governance State Machine (GSM) ZK Circuit

The GSM ZK Circuit provides a succinct, non-interactive proof that a transition from `State_t` to `State_{t+1}` is valid according to the GDL Master Canon.

### 1.1 Constraint System (R1CS / PLONKY2 / AIR)

The circuit enforces the following arithmetic constraints to ensure transition validity:

1.  **G-SRI Scoring Binding:**
    *   Let `T` be the set of raw telemetry traces (private input).
    *   Let `S` be the `Aggregated_Risk_Score` (public input).
    *   Constraint: `ComputeGSRI(T) - S = 0`.
    *   This is implemented via a recursive PLONKY2 sub-proof that ensures the score was derived from the traces using the formally defined scoring function.
2.  **State Transition Logic:**
    *   Let `St` be the current state and `St+1` be the next state.
    *   **Refusal Gating:** `IF S >= 0.85 THEN St+1 = CONTINUATION_REFUSAL_STATE`.
    *   **Integrity Gating:** `IF TPM_Attestation_Fail(PCR) THEN St+1 = LOCKED`.
    *   **Omega Gating:** `IF Valid_Omega_Sig(Sig) THEN St+1 = PLANETARY_HALT`.
3.  **Merkle Consistency:**
    *   Constraint: `MerkleVerify(Root_t, St, Path) = TRUE`.
    *   Ensures that the transition starts from a state already anchored in the immutable log.

### 1.2 Public vs. Private Inputs
*   **Public Inputs:** `Current_State`, `Target_State`, `Root_Hash_t`, `Root_Hash_{t+1}`, `Aggregated_Risk_Score`.
*   **Private Inputs:** Raw telemetry traces, individual agent SPIFFE IDs, specific GDL rule identifiers, TPM PCR values, OmegaActual signature components.

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
