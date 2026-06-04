# Omni-Sentinel CEE Architecture
**Containment Mesh: Three-Tier Isolation**

## 1. Sentinel Sidecars (Logical)
Intercepts all gRPC reasoning turns for GDL policy enforcement.

## 2. Minimal Governance Kernels (Kernel)
Nitro Enclave isolation with PCR-Match attestation.

## 3. IRMI Hardware Kill-Switches (Physical)
Hard-kill authority (INT 0x1A) capable of disconnecting DC power rails.
