# Technical Specification: GSM ZK Circuits & PQC WORM Logger
**Status:** CANONICAL // HIGH-ASSURANCE DRAFT
**Version:** 2.4.1
**Reference:** `src/infrastructure/pqc_worm_logger.py`, `src/infrastructure/zk_verifier.py`

## 1. Governance State Machine (GSM) ZK Circuit

The GSM ZK circuit ensures that all governance state transitions are valid according to the GDL (Governance Description Language) Master Canon.

### 1.1 Circuit Architecture: Plonky2 (AIR)
We utilize **Plonky2** for its superior recursion performance and sub-second proving times on standard hardware.
- **Field:** Goldilocks Field ($p = 2^{64} - 2^{32} + 1$).
- **Arithmetization:** Algebraic Intermediate Representation (AIR).
- **Commitment Scheme:** FRI-based Merkle Tree for PQC-resistance.

### 1.2 Constraint Definitions
- **Policy Invariant:** For any state transition $(S, S')$, $P(S') = \text{TRUE}$, where $P$ is the OPA/Rego compliance predicate.
- **Compute Binding:** $FLOP_{total} \le 10^{26}$, enforced via range proofs.
- **G-SRI Consistency:** $G\_SRI(t) = \text{BayesianSynthesis}(\text{Telemetry}(t))$.

## 2. PQC WORM Logger (Post-Quantum Cryptography)

The **PQC WORM Logger** provides an immutable, post-quantum secure audit trail.

### 2.1 Cryptographic Primitives
- **Signature Algorithm:** ML-DSA-87 (CRYSTALS-Dilithium-v3).
- **Hash Function:** SHA3-512 (Keccak) for Merkle leaf computation.
- **Domain Separation:**
    - `0x00`: Telemetry Leaf
    - `0x01`: Governance Decision Leaf

### 2.2 Persistence Architecture
1. **Ingestion:** Kafka WORM-Topic (Retention: Infinite).
2. **Buffering:** Bounded memory-pool for batch signing (max 1000 entries or 60 seconds).
3. **Commit:** AWS S3 Object Lock (Compliance Mode).
4. **Anchoring:** Root hash periodically anchored to Ethereum Mainnet (using `OmegaActual.sol`).

### 2.3 `pqc_worm_logger.py` Logic Flow
```python
def log_entry(self, payload):
    # 1. Salted SHA-256 for PII protection
    protected_payload = self.hash_pii(payload)
    # 2. ML-DSA-87 Signature
    sig = self.ml_dsa_sign(protected_payload)
    # 3. Append to Kafka/S3
    self.sink.write(protected_payload, sig)
```

## 3. Integrated Verification Loop
The **ZKVerifier** (`src/infrastructure/zk_verifier.py`) performs a combined check:
1. Verify the Plonky2 proof of state transition.
2. Verify the ML-DSA-87 signature of the corresponding log entry.
3. Confirm the S3 Object Lock status for the log batch.

## 4. Conclusion
This dual-layer cryptographic defense ensures that AI governance is both mathematically verifiable and post-quantum immutable.

---
**Verified By:** Jules-Apex
**Timestamp:** 2026-06-18T12:00:00Z
