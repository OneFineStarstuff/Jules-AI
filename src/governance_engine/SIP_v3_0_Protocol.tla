--------------------------- MODULE SIP_v3_0_Protocol ---------------------------
EXTENDS Integers, Sequences, FiniteSets

CONSTANTS
    Institutions,    \* Set of participating institutions
    Roots,           \* Set of GIEN root nodes
    MaxTreeSize,     \* Maximum Merkle tree size for simulation
    MaxMissing       \* Maximum missing STH windows before flagging

VARIABLES
    inst_sth,        \* inst_sth[inst] = current STH (sequence of hashes) published by institution
    root_log,        \* root_log[root][inst] = sequence of STHs seen by a root for a specific institution
    observed_missing,\* observed_missing[inst] = number of consecutive missing STH windows
    system_state     \* {"OK", "EQUIVOCATION_DETECTED", "MISSING_ATTESTATION"}

vars == <<inst_sth, root_log, observed_missing, system_state>>

TypeOK ==
    /\ system_state \in {"OK", "EQUIVOCATION_DETECTED", "MISSING_ATTESTATION"}
    /\ inst_sth \in [Institutions -> Seq(Integers)]
    /\ root_log \in [Roots -> [Institutions -> Seq(Integers)]]

Init ==
    /\ inst_sth = [i \in Institutions |-> <<>>]
    /\ root_log = [r \in Roots |-> [i \in Institutions |-> <<>>]]
    /\ observed_missing = [i \in Institutions |-> 0]
    /\ system_state = "OK"

\* Institution publishes a new STH (Signed Tree Head)
PublishSTH(inst, hash) ==
    /\ Len(inst_sth[inst]) < MaxTreeSize
    /\ inst_sth' = [inst_sth EXCEPT ![inst] = Append(@, hash)]
    /\ observed_missing' = [observed_missing EXCEPT ![inst] = 0]
    /\ UNCHANGED <<root_log, system_state>>

\* Operator to detect equivocation for a specific institution
IsEquivocating(root, inst, next_sth, next_idx) ==
    \E r \in Roots :
        /\ Len(root_log[r][inst]) >= next_idx
        /\ root_log[r][inst][next_idx] /= next_sth

\* Root node gossips/pulls an STH from an institution
GossipSTH(root, inst) ==
    LET published == inst_sth[inst]
        seen == root_log[root][inst]
        next_idx == Len(seen) + 1
    IN
    /\ next_idx <= Len(published)
    /\ LET next_sth == published[next_idx]
       IN
       /\ system_state' = IF IsEquivocating(root, inst, next_sth, next_idx)
                          THEN "EQUIVOCATION_DETECTED"
                          ELSE system_state
       /\ root_log' = [root_log EXCEPT ![root][inst] = Append(@, next_sth)]
    /\ observed_missing' = observed_missing
    /\ inst_sth' = inst_sth

\* Simulate a missing window for an institution
SkipWindow(inst) ==
    /\ observed_missing[inst] < MaxMissing
    /\ observed_missing' = [observed_missing EXCEPT ![inst] = @ + 1]
    /\ system_state' = IF observed_missing'[inst] = MaxMissing
                       THEN "MISSING_ATTESTATION"
                       ELSE system_state
    /\ UNCHANGED <<inst_sth, root_log>>

Next ==
    \/ \E i \in Institutions : \E h \in Integers : PublishSTH(i, h)
    \/ \E r \in Roots, i \in Institutions : GossipSTH(r, i)
    \/ \E i \in Institutions : SkipWindow(i)

\* Invariant: No Silent Divergence
NoSilentDivergence ==
    \A i \in Institutions :
        \A r1, r2 \in Roots :
            LET log1 == root_log[r1][i]
                log2 == root_log[r2][i]
                min_len == IF Len(log1) < Len(log2) THEN Len(log1) ELSE Len(log2)
            IN \A idx \in 1..min_len : log1[idx] = log2[idx] \/ system_state = "EQUIVOCATION_DETECTED"

\* Liveness: Root Convergence
RootConvergence ==
    \A i \in Institutions :
        \A r \in Roots :
            Len(root_log[r][i]) = Len(inst_sth[i]) \/ system_state /= "OK"

Liveness ==
    /\ \A i \in Institutions : WF_vars(SkipWindow(i))
    /\ \A r \in Roots, i \in Institutions : WF_vars(GossipSTH(r, i))

Spec == Init /\ [][Next]_vars /\ Liveness

=============================================================================
