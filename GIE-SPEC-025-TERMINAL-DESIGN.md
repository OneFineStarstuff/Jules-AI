# GIE-SPEC-025: High-Assurance Terminal Visual Design Guide
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Aesthetic Philosophy
The **Omni-Sentinel Governance Cockpit** must utilize the **High-Assurance Terminal** aesthetic to minimize cognitive load and reinforce the gravity of institutional oversight.

## 2. Palette & Typography
- **Primary Background:** Deep Onyx (#020617)
- **Accent Color:** Governance Blue (#1e3a8a)
- **Alert Tiers:**
  - **T1/T2:** Amber (#f59e0b)
  - **T3/T4:** Crimson (#b91c1c)
- **Typography:** Inter (San-Serif) for readability; JetBrains Mono for telemetry streams.

## 3. UI Components
- **GSRIDriftSimulator:** Real-time Bayesian update chart with gradient safety-zones.
- **AgentReasoningDAG:** React Flow visualization of goal-decomposition, color-coded by RIG Family.
- **SafetyProtocolHeadsUp:** Persistent sidebar showing active OPA-Rego status and TPM/PCR_MATCH.

## 4. Accessibility
All terminal views must satisfy **WCAG 2.1 AA** standards. High-contrast modes and screen-reader support are mandatory for all regulatory-facing reports.

## 5. Interaction Patterns
- **Latency:** UI interaction must respond in < 100ms.
- **Quorum UI:** Special multi-signature interface for GBEC board-level interventions, requiring concurrent presence of 3-of-5 authorized operators.
