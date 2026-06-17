# Team Rehearsal Plan: 90-Minute Regulator Demo

**Focus:** Technical Rigor, Smooth Handoffs, and Verifiable Trust.

## 1. Timing & Handoffs
- **[00:00] Lead Architect:** Vision & Architecture.
- **[00:15] Compliance Lead:** GSM States & Regulatory Mapping.
- **[00:35] DevSecOps Lead:** Live GDL Violation & IRMI Trigger.
- **[00:55] Security Engineer:** Evidence Pipeline & ZK-Proof Verification.
- **[01:15] Moderator:** Q&A.

## 2. Live Tooling Segments
- **Segment A:** CLI demonstration of `sentinel-verify` on the Merkle STH.
- **Segment B:** TLA+ Toolbox walkthrough showing TLC checking Scenario 2 (Equivocation).
- **Segment C:** Real-time G-SRI dashboard monitoring during the "Dragon-Beta" shock.

## 3. Rehearsal Checklist
- [ ] AMD SEV-SNP enclave initialized and attested.
- [ ] Kafka brokers pre-loaded with mock high-risk traces for Scenario 2.
- [ ] TLA+ spec loaded with minimal model for sub-5s TLC result.
- [ ] Digital Takeaway Packets staged in the Regulator Evidence Vault.

## 4. Fallback Drills
- **Hiccup:** Demo UI latency. **Tactic:** Switch to "Shadow Dashboard" (pre-rendered static view).
- **Hiccup:** ZK Prover timeout. **Tactic:** Load "Pre-computed Evidence Pack" from Q1.
- **Hiccup:** Network loss. **Tactic:** Local sandbox VM for all CLI commands.

## 5. Q&A Roleplay
- **Persona: The Skeptical Auditor.** "How do I know the ZK circuit isn't forged?"
    - *Ans:* By re-verifying the proof against the public circuit parameters using the independent Verifier Node.
