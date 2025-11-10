# A.O.A.I Private Owner's Manual

**Classification:** Internal - Privileged Operators Only

## 1. Overview
This manual describes privileged workflows for operating the A.O.A.I platform, including key management, incident response, and compliance attestations. Distribution is restricted to vetted operators bound by the Alpha Access NDA.

## 2. Access Control
- Maintain operator accounts in hardware-backed password manager with MFA.
- Rotate master HMAC signing keys every 180 days; record fingerprints in `key_registry.yml`.
- Use offline signing workstation to authorize new releases.

## 3. Deployment Steps
1. Provision dedicated VM or enclave with TPM and secure boot.
2. Install dependencies via `make bootstrap` (requires Python 3.10+, OpenSSL 3, libffi, sqlite3).
3. Run `aoai-cli install` to create systemd services for LSA and Truth Engine.
4. Configure `.env.production` with license tier, telemetry endpoint, and legal contacts.
5. Execute `aoai-cli verify` to confirm license compliance and key signatures.

## 4. Incident Response Workflow
- When suspicious event triggers, SOC analyst reviews `aoai_audit.db` via `aoai-cli audit view --since 24h`.
- If confirmed violation, export evidence: `aoai-cli audit export --case CASEID --bundle bundle.zip`.
- Escalate per legal escalation matrix; notify privacy officer within 1 hour.
- File transparency event within 24 hours; include anonymized statistics.

## 5. Maintenance
- Apply security patches monthly; run `make regression` post-update.
- Review K-Math invariant logs weekly to detect drift or tampering.
- Archive logs older than 90 days to encrypted cold storage (AES-256, key split via Shamir secret sharing).

## 6. Compliance Checklist
- SOC2 controls mapped to operational procedures (Appendix A).
- ISO 27001 Annex A controls documented with evidentiary links.
- GDPR & CCPA data subject request workflows validated quarterly.

## 7. Emergency Shutdown
- `aoai-cli lockdown` disables all external telemetry, revokes API tokens, and enforces manual approval for any permission changes.
- Broadcast emergency notice to users with recommended safety steps.
- Document timeline and rationale for audit committee.

## 8. Appendices
- Appendix A: Control mapping spreadsheet template.
- Appendix B: Legal escalation contact roster (stored securely, not in repo).
- Appendix C: Change management form template.
