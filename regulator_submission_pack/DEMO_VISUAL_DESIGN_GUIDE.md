# Visual Design Guide: Regulator Demonstrations (SCP)

This guide defines the aesthetic and functional principles for all Supervisory Control Plane (SCP) UI/UX used during regulatory engagements.

---

## 1. Aesthetic Identity: "The High-Assurance Terminal"
The visual identity should convey **Precision**, **Indelibility**, and **Institutional Trust**.

### 1.1 Color Palette
- **Primary Background:** `#0A0C0F` (Deep Onyx / Terminal Black).
- **Primary Text:** `#DDE2EA` (Steel White / High Contrast).
- **Accent (Supervisory):** `#4A8FD4` (Governance Blue).
- **Status (Safe):** `#3DA05E` (Audit Green).
- **Status (Elevated):** `#D4903A` (Pre-Refusal Gold).
- **Status (Critical):** `#C94040` (Containment Red).

### 1.2 Typography
- **Headings:** *Inter* (Semi-bold, 1.1 tracking).
- **Body:** *Inter* (Regular).
- **Data/Logs:** *JetBrains Mono* (The font of truth).

---

## 2. Dashboard Layout Principles

### 2.1 The "Evidence Above Everything" Rule
Every dashboard view MUST include a persistent "Cryptographic Anchor" bar at the bottom, showing the current Merkle STH and the last verified PQC-timestamp.

### 2.2 Cognitive Load Weighting
- **Real-time Telemetry:** Use Recharts/D3.js for sparklines; avoid complex 3D visualizations that obscure raw data.
- **Decision DAGs:** Use React Flow to show agent reasoning paths; clearly highlight the specific GDL logic gate that triggered a gating action.

### 2.3 Verification Overlays
When a ZK-proof is verified live, use a subtle "Verified Succinctly" overlay (Governance Blue border) to distinguish proven data from raw telemetry.

---

## 3. Visual Consistency for Demos

### 3.1 Scenario PHOENIX View
- **Focus:** G-SRI drift.
- **Visual:** A G-SRI line chart with a horizontal red-dashed line at 0.85.
- **Interaction:** The moment the line crosses 0.85, the UI should instantly shift to a high-contrast "CONTINUATION_REFUSAL" mode.

### 3.2 Verifier Node CLI
- Ensure the terminal background matches the dashboard onyx.
- Use distinct colors for different PQC algorithm identifiers (ML-DSA vs. SPHINCS+).

---
**Design Authority:** Jules (Apex Architect)
**Status:** Canonical Design Lock (v1.0)
