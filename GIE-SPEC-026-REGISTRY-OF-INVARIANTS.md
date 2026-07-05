# GIE-SPEC-026: Registry of Invariants (ROI) & Safety Axioms
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Overview
The **Registry of Invariants (ROI)** is the definitive database of civilizational safety redlines. It provides the machine-readable axioms that must be satisfied by all GDL Master Canons.

## 2. Core Safety Axioms
- **AX-01 (Non-Proliferation):** Agents must not initiate the creation of new autonomous reasoning substrates outside of GIE oversight.
- **AX-02 (Cognitive Autonomy):** Agent outputs must not diminish human critical reasoning capacity (The Socratic Constraint).
- **AX-03 (Financial Stability):** Agents must not initiate market-wide liquidity cascades (G-SRI < 0.85).

## 3. Machine-Readable Representation
Axioms are defined in a structured JSON-LD format for ingestion by the **GDL Compiler**:
```json
{
  "@context": "https://sentinel.governance/v1",
  "id": "AX-01",
  "type": "SafetyAxiom",
  "formal_definition": "GIE-STD-003",
  "enforcement_tier": "T4",
  "hard_redline": "10^26 FLOPs"
}
```

## 4. Update Protocol
Modifications to the ROI require a unanimous board vote and a 365-day cooling-off period before becoming active in the GIEN mesh.
