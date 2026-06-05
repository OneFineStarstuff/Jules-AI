# GAI-SOC Telemetry Specification (v1.0)
**Interface:** R-SGQL (Resilient Sentinel Graph Query Language)

## 1. Telemetry Ingestion
- **Source:** Sentinel Sidecars (Envoy/Istio).
- **Format:** Protobuf defined in `/schemas/telemetry.proto`.
- **Latency:** P99 E2E latency < 200ms.

## 2. Global Systemic Risk (G-SRI) Feed
Centralized Bayesian aggregator that updates the institutional G-SRI every 1s based on global drift signals.
