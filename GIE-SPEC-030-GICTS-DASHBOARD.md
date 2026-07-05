# GIE-SPEC-030: GICTS Control Effectiveness Dashboard Design
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Overview
The **GICTS Dashboard** provides real-time visualization of the effectiveness of all technical governance controls across the institutional mesh.

## 2. Key Performance Indicators (KPIs)
- **Mean Time to Containment (MTTC):** Average time from threshold breach to GIRI enforcement (Target < 200ms).
- **Attestation Health:** Percentage of enclaves with valid PCR_MATCH (Target 100%).
- **WORM Sync Fidelity:** Lag time between GEE events and PQC-WORM anchoring (Target < 60s).
- **ZK-Proof Throughput:** Proofs generated per second per enclave cluster.

## 3. Visualization Components
- **Control-Heatmap:** A grid showing control status (Pass/Fail) across all RIG Families.
- **Latency-Spectrum:** Distribution of containment latencies for simulated breaches.
- **Resonance-Drift-Cloud:** Vector visualization of goal-intent clusters compared to the golden policy anchor.

## 4. Regulatory View
A dedicated, WCAG 2.1 AA compliant view is provided for regulatory auditors, enabling them to drill down into specific **GIRS** reports and forensic reconstructions (GIE-SPEC-027).
