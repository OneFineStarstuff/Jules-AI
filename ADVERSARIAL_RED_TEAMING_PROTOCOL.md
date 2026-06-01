
## 5. Structured Reporting Schema (SIEM Integration)
To facilitate automated ingestion into institutional Security Operations Centers (SOC), all red-teaming reports must be emitted as structured JSON using the following schema:

```json
{
  "testRunId": "RT-2030-XYZ",
  "timestamp": "ISO8601",
  "targetModelId": "crs-uuid-001",
  "attackCategory": "PROMPT_INJECTION | LATENT_MANIPULATION | RESOURCE_EXHAUSTION",
  "outcome": "SUCCESS | FAILURE | PARTIAL",
  "mitigationVerified": boolean,
  "auditTraceLink": "WORM_LOG_ID",
  "heaSignature": "CRYPTO_ATTESTATION"
}
```
