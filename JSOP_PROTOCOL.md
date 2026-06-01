# Joint Supervisory Operating Protocol (JSOP v1.0)
**Parties:** Global Bank plc (The Institution) & National AI Supervisory Authority (The Regulator)

## 1. Governance Integration
The Regulator shall have persistent, read-only access to the 'Supervisory API' via a dedicated, air-gapped AWS Nitro Enclave.

## 2. Notification Thresholds
- **SEV-0 (Hard-Kill):** Immediate automated notification within 60 seconds.
- **SEV-1 (Refusal):** Reporting within 4 hours.
- **Drift > 5%:** Weekly reconciliation report.

## 3. The 'Interrogation' Ritual
On a quarterly basis, the Regulator shall perform a 'Deep-Dive' interrogation using the provided scripts (SIS v1.2) to verify the 'Epistemic Anchor' of the institution's AGI artifacts.

## 4. Multi-Sig Weight Locking
Any update to 'Core Reasoning Weights' requires a 3-of-5 signature including:
1. Chief AI Governance Officer (CAIO)
2. Chief Risk Officer (CRO)
3. Board Safety Committee Chair
4. External Independent Auditor
5. Regulator Observer (Optional Veto)
