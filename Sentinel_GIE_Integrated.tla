---------------- MODULE Sentinel_GIE_Integrated ----------------
EXTENDS Naturals, Reals, Sequences

VARIABLES
    enclaves,       \* State of hardware enclaves
    gsri_score,     \* Real-time systemic risk index
    audit_log,      \* Sequence of PQC-WORM signatures
    mesh_state      \* Global mesh status

\* Constants
CONSTANT MAX_GSRI, ENCLAVE_COUNT, SUCCESS, FAILURE, UNKNOWN

TypeOK ==
    /\ enclaves \in [1..ENCLAVE_COUNT -> {SUCCESS, FAILURE, UNKNOWN}]
    /\ gsri_score \in 0..100
    /\ audit_log \in Seq(STRING)
    /\ mesh_state \in {"ACTIVE", "DEGRADED", "CONTAINED"}

\* Initial State
Init ==
    /\ enclaves = [i \in 1..ENCLAVE_COUNT |-> UNKNOWN]
    /\ gsri_score = 10
    /\ audit_log = <<>>
    /\ mesh_state = "ACTIVE"

\* Step 1: Enclave Attestation
Attest(i) ==
    /\ enclaves[i] = UNKNOWN
    /\ enclaves' = [enclaves EXCEPT ![i] = SUCCESS]
    /\ UNCHANGED <<gsri_score, audit_log, mesh_state>>

\* Step 2: GSRI Update & Audit Commit
UpdateRisk(s) ==
    /\ mesh_state = "ACTIVE"
    /\ gsri_score' = s
    /\ audit_log' = Append(audit_log, "ML-DSA-87-SIG")
    /\ IF s > MAX_GSRI THEN mesh_state' = "CONTAINED" ELSE mesh_state' = "ACTIVE"
    /\ UNCHANGED <<enclaves>>

Next ==
    \/ \E i \in 1..ENCLAVE_COUNT : Attest(i)
    \/ \E s \in 0..100 : UpdateRisk(s)

\* Safety Invariant: If GSRI exceeds limit, system must be contained.
GSRI_Safety == gsri_score > MAX_GSRI => mesh_state = "CONTAINED"

-----------------------------------------------------------------
