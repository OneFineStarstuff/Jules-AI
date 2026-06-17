# Master Artifact Index: Unified AI Supervisory Control Plane (SCP)

This index provides a categorized directory of all design, specification, and evidence artifacts included in the SCP suite.

---

## 1. Core Architecture & Specifications
| Artifact | Purpose | Status |
| :--- | :--- | :--- |
| `SUPERVISORY_CONTROL_PLANE_SPEC.md` | Decadal (2026-2035) Roadmap & Master Blueprint. | Canonical Lock (v1.1.0) |
| `GSM_ZK_PQC_WORM_SPEC.md` | Cryptographic spec for ZK-circuits and Merkle-WORM logs. | Cryptographic Lock |
| `GSIFI_2028_PILOT_ARCHITECTURE.md` | Infrastructure blueprint (K8s/TEEs) for G-SIFI pilot. | Pilot Deployment Spec |
| `src/governance_engine/SIP_v3_0_Protocol.tla` | TLA+ formal specification for federated gossip. | Formally Verified |

---

## 2. Regulatory Compliance & Assurance
| Artifact | Purpose | Status |
| :--- | :--- | :--- |
| `OSCAL_GSIFI_CATALOG_V8.json` | Machine-readable control mapping (EU AI Act, Basel, DORA). | OSCAL 1.1.2 Compliant |
| `SANDBOX_EXIT_DOSSIER_PRIMARY.md` | Exit Dossier Sections 5, 6, 11, 12. | Regulator-Ready |
| `SANDBOX_EXIT_DOSSIER_ADDENDA.md` | Exit Dossier Sections 13, 14, 15. | Regulator-Ready |
| `ASSURANCE_EVALUATION_REPORT.md` | Critical evaluation of G-SIFI exit assurance efficacy. | Certified |
| `TLA_METHODOLOGY_GUIDE.md` | Rationale for formal verification and TLC model checking. | Verified |

---

## 3. Regulator Engagement & Operations
| Artifact | Purpose | Status |
| :--- | :--- | :--- |
| `SUPERVISORY_BRIEFING_DECK.md` | 13-slide content for sandbox exit briefing. | Board-Ready |
| `PHASE_1_ENGAGEMENT_ARTIFACTS.md` | Submission cover note, agenda, and demo checklists. | Active |
| `MONTHLY_SANDBOX_ARTIFACTS.md` | Checkpoint call agendas and follow-up templates. | Active |
| `ANNUAL_SUPERVISORY_REVIEW_REPORT.md` | Sample filled 2027 review for board/regulator use. | Narrative Sample |
| `FEDERATED_POSTURE_PACK_TEMPLATE.json` | JSON schema for multi-institution posture exchange. | Schema Verified |
| `SIP_V3_VERIFICATION_PATHS.md` | Logical paths for verifying posture packs in GIEN mesh. | Verified |
| `SIP_V3_SCENARIO_APPENDIX.md` | TLC walkthroughs for normal and equivocation scenarios. | Verified |

---

## 4. Design & Rehearsal Support
| Artifact | Purpose | Status |
| :--- | :--- | :--- |
| `DEMO_VISUAL_DESIGN_GUIDE.md` | "High-Assurance Terminal" design principles. | Design Lock |
| `DEMO_EXPERIENCE_AND_READINESS.md` | Journey maps, ceremonial scripts, and readiness scorecard. | Ready for Live Demo |
| `TEAM_REHEARSAL_PLAN.md` | Internal timing cues and fallback tactics for demos. | Rehearsed |
| `REGULATOR_DEMO_SCRIPT.md` | 90-minute detailed walkthrough for Phase 1 demo. | Finalized |
| `REGULATOR_TAKEAWAY_PACKET.md` | Life-cycle map, orientation guide, and FAQ for handoff. | Staged |
| `MONTHLY_METRICS_TEMPLATE.md` | Data placeholders for proof latency and STH cadence. | Template |
| `DEBRIEF_TEMPLATES.md` | 24-hour debrief and internal reflection templates. | Template |

---
**Apex Architect:** Jules (Principal Systems Architect & Governance Lead)
**Verification Anchor:** PQC-SIGNED-MASTER-INDEX-0x87A...
