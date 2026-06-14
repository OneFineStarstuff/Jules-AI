# IRMI: Integrated Risk Mitigation Interface Protocol Specification

## 1. Hardware-Software Interface
The IRMI protocol defines the low-latency communication path between the Sentinel Reasoning Kernel and the physical compute substrate.

## 2. INT 0x1A: The Safety Interrupt
- **Interrupt Vector:** 0x1A.
- **Trigger Condition:** Evaluated by the GDL sidecar in the Trusted Execution Environment (TEE).
- **Action:** Immediate hardware-level isolation of the GPU power rail.
- **Latency Target:** < 1ms from detection to severance.

## 3. Atomic State Locking
Once the IRMI interrupt is fired:
1. **Volatile Memory Purge:** All VRAM containing reasoning weights is zeroed out.
2. **State Suspension:** The instruction pointer is locked in a `LOCKED` loop.
3. **Multi-sig Unlock:** Recovery requires a 3-of-5 cryptographic multisig from the Sovereign Governance Board.

---
**Status:** HARDWARE CANON v1.0.0
