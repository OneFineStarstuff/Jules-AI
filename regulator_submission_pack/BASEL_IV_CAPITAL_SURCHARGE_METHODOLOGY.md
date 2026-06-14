# Basel IV: AGI Systemic Risk Capital Surcharge Methodology

## 1. Calculation Engine
Capital surcharges for G-SIFIs are dynamically indexed to the **Global Systemic Risk Index (G-SRI)**.

## 2. Surcharge Brackets
| G-SRI Range | Risk Classification | Capital Add-on (bps) |
| :--- | :--- | :--- |
| **0.00 - 0.20** | NOMINAL | 0 |
| **0.20 - 0.50** | ELEVATED | 50 |
| **0.50 - 0.85** | CRITICAL | 250 |
| **> 0.85** | REDLINE | Immediate Cease & Desist |

## 3. Enforcement
The **Fiduciary Guardrail Engine** blocks any transaction that would result in a capital requirement exceeding the institution's Liquidity Coverage Ratio (LCR) as adjusted by the real-time G-SRI.

---
**Status:** PRUDENTIAL STANDARD v1.4
