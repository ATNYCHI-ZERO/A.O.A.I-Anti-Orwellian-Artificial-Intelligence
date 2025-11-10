# Safety Case Summary

## System Definition
- **System:** A.O.A.I defensive AI platform.
- **Operational Context:** On-device monitoring, browser protection, truth verification, and legal reporting for government agencies.

## Hazard Identification
| Hazard | Description | Mitigation |
|--------|-------------|------------|
| H1 | Unauthorized biometric capture bypasses consent | LSA permission broker, audit alerts, hardware controls |
| H2 | Truth engine hallucination or false citation | K-Math invariants, retrieval grounding, human review loop |
| H3 | Evidence tampering | HMAC-SHA256 signatures, append-only ledger, verification CLI |
| H4 | Privacy violation through telemetry | Opt-in telemetry, data minimization policies, encryption |
| H5 | Offensive misuse | Constitutional-AI License, runtime compliance checks, monitoring |

## Assurance Arguments
- **Safety Goal SG1:** Prevent unauthorized access to user biometrics.  
  - *Strategy:* Enforce default deny, monitor processes via psutil, respond via policy engine.  
  - *Evidence:* Unit tests (`tests/test_lsa.py`), audit logs, permission request logs.
- **Safety Goal SG2:** Guarantee truthful responses with verifiable evidence.  
  - *Strategy:* Retrieval pipeline, citation requirement, K-Math distribution checks.  
  - *Evidence:* Truth engine test cases, manual evaluations, citation coverage reports.
- **Safety Goal SG3:** Maintain tamper-evident audit trails.  
  - *Strategy:* Signed ledger, SHA-256 hashing, verification CLI.  
  - *Evidence:* `tests/test_audit.py`, signed export samples.

## Residual Risk
Residual risk is considered low given mitigations. Operators must continuously monitor ledger alerts and maintain compliance posture.

## Compliance Mapping
- NIST CSF: ID.AM-2, PR.AC-4, DE.AE-2, RS.CO-1.  
- FedRAMP Moderate: AC-6, AU-2, AU-10, IR-6.  
- Privacy: GDPR Articles 5, 12, 25; CCPA §1798.100.

## Verification & Validation
- Automated tests executed per release (`make test`).
- Independent penetration tests annually.
- Government witness testing prior to production deployment.
