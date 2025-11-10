# Privacy Impact Assessment (PIA) Template

## 1. System Overview
- System Name: A.O.A.I — Anti-Orwellian Artificial Intelligence
- System Owner: A.O.A.I Collective
- Purpose: Detect and block unauthorized biometric access, provide truthful AI responses, maintain audit trails.

## 2. Data Inventory
| Data Type | Source | Retention | Protection |
|-----------|--------|-----------|------------|
| Biometric access attempts | Local OS hooks | 90 days (rotating) | AES-256 encrypted, signed entries |
| Consent status | User-provided | Lifetime of session | In-memory, not persisted unless audit event |
| Audit logs | Generated events | 1 year | SQLite + HMAC-SHA256 signatures |
| Knowledge pack references | Curated dataset | Until update | Hashed, integrity-checked |

## 3. Legal Authorities
- GDPR Articles 6(1)(c), 6(1)(f) for legitimate interest in security.
- CCPA §1798.105 (opt-out and deletion support).
- Applicable agency privacy statutes.

## 4. Privacy Risks & Mitigations
- **Risk:** Unauthorized disclosure of audit logs.  
  *Mitigation:* Encrypted storage, access controls, role-based permissions.
- **Risk:** Over-collection of biometric data.  
  *Mitigation:* Default deny policy; only metadata stored. No raw biometric payloads retained.
- **Risk:** Cross-border data transfers.  
  *Mitigation:* Local-first design; if telemetry enabled, processed in-region per contract.

## 5. Data Subject Rights
- Provide self-service portal for access, correction, deletion requests.
- Log responses and completion times for compliance audit.

## 6. Security Controls
- Encryption in transit (TLS 1.3) and at rest (AES-256 GCM).
- Hardware-backed key storage optional for Sovereign tier.
- Continuous monitoring with signed logs and anomaly detection.

## 7. Accountability
- Privacy Officer responsible for compliance.
- Quarterly internal audits; annual third-party review.
- Breach notification procedures aligned with applicable law.

## 8. Approval
Prepared by: ____________________  Date: ____________
Reviewed by: ____________________  Date: ____________
Approved by: ____________________  Date: ____________
