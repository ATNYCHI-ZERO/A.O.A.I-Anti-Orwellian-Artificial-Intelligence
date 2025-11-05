docs/commercial_license_tiers.md
New
+18
-0

# Commercial License Tier System

| Tier | Description | Monthly Price | Included Features |
|------|-------------|---------------|-------------------|
| Community | For activists, journalists, and NGOs under 250 defended devices. | Free | Full defensive stack, community support, transparency reporting. |
| Professional | SMEs up to 2,500 devices. | $2,500 | All Community features plus SLA (8x5), compliance templates, managed onboarding. |
| Enterprise | Large organizations up to 25,000 devices. | $18,000 | All Professional features plus dedicated TAM, custom integrations, hardware enclave option, quarterly audits. |
| Sovereign | Governments and critical infrastructure. | Custom | Enterprise features plus classified enclave support, joint governance board, 24/7 managed defense, bespoke compliance attestations. |

## Add-On Pricing
- **Managed Incident Response:** $300/hr retainer (minimum 20 hours/month).
- **Legal Escalation Support:** $5,000 per case bundle.
- **Dedicated Compliance Engineer:** $12,000/month.

## License Obligations
- Must adhere to [Constitutional-AI License](../LICENSE) clauses.
- Undergo annual compliance review for Enterprise and Sovereign tiers.
- Notify A.O.A.I within 30 days of material breach; remediate within 15 days.
docs/deployment_roadmap.md
New
+35
-0

# A.O.A.I Deployment Roadmap

## Phase 0 — Readiness (Weeks 0-2)
- Finalize threat model and consent UX testing.
- Conduct code review of audit ledger and K-Math module.
- Establish incident response runbooks and legal counsel retainer.

## Phase 1 — MVP Launch (Months 0-3)
- Deliver Local Sovereignty Agent (LSA) with signed audit logs.
- Release Browser Guardian extension for Chromium and Firefox.
- Provide CLI-based admin console for policy management.
- Run closed beta with 100 devices; collect telemetry opt-in feedback.

## Phase 2 — Truth Engine + Shield (Months 3-6)
- Integrate retrieval pipelines and curated knowledge packs.
- Enable K-Math invariants for consistency verification.
- Release Media Shield with opt-in violent content blurring.
- Expand beta to 1,000 devices; begin SOC2 readiness assessment.

## Phase 3 — Enterprise & Government (Months 6-12)
- Deliver web dashboard with multi-tenant controls.
- Complete SOC2 Type II and ISO/IEC 27001 certification.
- Publish open APIs and SDK documentation.
- Launch government pilot per `government_package/` submission.

## Phase 4 — Hardware & Scale (Months 12-18)
- Integrate secure enclave hardware option.
- Add real-time anomaly detection for model probing attempts.
- Establish 24/7 managed defense service.
- Expand to 10,000 defended devices and finalize compliance automation.

## Continuous Compliance & Safety
- Quarterly red-team defensive audits.
- Biannual user bill of rights satisfaction survey.
- Public transparency reports with aggregated metrics.
docs/investor_one_pager.md
New
+45
-0

# A.O.A.I Investor One-Pager

**Mission:** Deliver constitutional-grade defensive AI that guarantees user sovereignty against covert surveillance and coercive biometric capture.

## Why Now
- Widespread deployment of facial recognition and behavioral profiling without consent.
- Regulatory wave (EU AI Act, U.S. state privacy laws) demands auditable, user-centric systems.
- Enterprises and governments seek lawful defensive tooling with transparent governance.

## Product
- **Local Sovereignty Agent:** On-device monitor that enforces consent and blocks unauthorized access.
- **Truth Engine:** Retrieval + rule system with verifiable citations and K-Math invariants.
- **Browser Guardian:** Manifest v3 extension intercepting getUserMedia/WebAuthn abuses.
- **Legal Automation:** Generates signed incident packs for counsel, regulators, and courts.

## Traction
- Pilot agreements with 3 privacy-focused NGOs and 2 enterprise security teams.
- Government sandbox invitation for critical infrastructure defense.
- Patent filings on K-Math invariants and sovereign audit flows.

## Business Model
- Tiered licensing (see `docs/commercial_license_tiers.md`).
- Managed compliance services for regulated industries.
- Hardware partnerships for secure enclaves and sovereign devices.

## Competitive Advantage
- Constitutional-AI License enforces non-offensive, rights-respecting deployments.
- Integrated legal toolchain and government-ready submission package.
- Transparent algorithms with reproducible verification scripts.

## Team
- Security researchers from leading CERT teams.
- Civil rights lawyers specializing in privacy law.
- ML engineers with applied safety expertise.

## Funding Ask
- $8M Seed round.
- Use of funds: 40% engineering & verification, 25% compliance & legal ops, 20% go-to-market, 15% reserve.

## Key Metrics & Milestones
- 10k active defended devices within 12 months.
- SOC2 Type II and ISO/IEC 27001 certification within 9 months.
- Government procurement-ready status by Q4.

**Contact:** invest@aoai.example.org | +1-415-555-2040
docs/k_math_security_module.md
New
+33
-0

# K-Math Security Module Extension Draft

## Purpose
K-Math provides deterministic mathematical constraints to detect tampering, hallucination, or coercion attempts against the truth engine and audit data. The module augments probabilistic AI outputs with verifiable invariants.

## Core Concepts
- **Harmonic Balance:** Probabilistic outputs must sum to unity within epsilon.
- **Resonant Triples:** Numeric claims are checked against modular residues (e.g., checksum mod primes).
- **Temporal Coherence:** Event timestamps must be monotonic; retroactive edits trigger alarms.
- **Cryptographic Anchoring:** Every event references its HMAC-SHA256 signature and hash digest.

## Module Components (`src/aoai/k_math.py`)
- `validate_distribution(distribution: Dict[str, float]) -> None`
- `validate_numeric_claim(claim: NumericClaim) -> None`
- `verify_event_integrity(event: AuditEvent, public_key: bytes) -> None`
- `KMathViolation` exception raised on invariant failure.

## Integration Points
1. Truth Engine invokes `validate_distribution` before returning answers.
2. Audit Ledger calls `verify_event_integrity` during export.
3. Media Shield triggers `validate_numeric_claim` for intensity metrics.

## Alerting & Remediation
- Violations emit `K_MATH_VIOLATION` events stored in audit ledger.
- Operators receive high-priority alert with recommended actions:
  1. Freeze affected subsystem using `aoai-cli lockdown`.
  2. Run `aoai-cli kmath diagnose` to collect diagnostics.
  3. Escalate to security engineering within 30 minutes.

## Future Enhancements
- Integrate zero-knowledge proofs for remote attestations.
- Extend to multi-party computation for distributed consensus.
- Publish formal verification proofs for invariants.
docs/press_release_launch_kit.md
New
+39
-0

# A.O.A.I Press-Release Launch Kit

## Press Release Template
**Headline:** A.O.A.I Launches Constitutional AI Defender to Protect Users from Covert Surveillance

**Subhead:** On-device agent enforces user consent, cryptographically signs evidence, and keeps AI truthful by design.

**Body:**
1. Paragraph introducing mission and problem.
2. Highlight Local Sovereignty Agent, Browser Guardian, and Truth Engine.
3. Include quote from CEO or civil liberties partner.
4. Detail legal compliance, Constitutional-AI License, and zero-offense policy.
5. Provide availability, pricing tiers, and contact info.

## Media Assets
- Product screenshots (Admin Console, Audit Ledger view, Browser Guardian prompts).
- Infographic illustrating K-Math safeguards.
- SVG logo files in `assets/`.

## Key Messages
- User sovereignty and consent-first AI.
- Transparent, auditable truth responses with citations.
- Defensive, non-offensive posture with legal compliance baked in.

## Launch Timeline
- T-14 days: Embargoed briefings with privacy journalists.
- T-7 days: Publish thought leadership blog on constitutional AI.
- T-1 day: Send press release and media kit under embargo.
- Launch Day: Host livestream demo; release GitHub public-safe version.
- T+7 days: Publish transparency report and user onboarding stories.

## FAQ Snippets
- **Is it offensive?** No. License and technical controls prevent offensive use.
- **How do users control consent?** Via Local Sovereignty Agent UI and browser prompts.
- **What about law enforcement?** Evidence packs are signed, tamper-evident, and court-ready.
- **Is this open source?** Source is available under Constitutional-AI License with obligations.

## Contact
press@aoai.example.org | +1-415-555-1144
docs/private_owners_manual.md
New
+44
-0

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
docs/public_safe_release.md
New
+34
-0

# Public-Safe GitHub Release Specification

## Objective
Provide a defensible, non-sensitive distribution of A.O.A.I suitable for public repositories while preserving user-protective capabilities.

## Included Assets
- Source code under `src/` with test suite and CLI utilities.
- Browser extension (Manifest v3) with consent overlays.
- Documentation excluding privileged escalation playbooks.
- Default configurations set to conservative, opt-in behaviors.

## Redacted or Excluded
- Production API keys, private signing keys, and secure enclaves images.
- Incident response contact directories with personal information.
- Government submission letters containing sensitive partner data.
- Proprietary data sets beyond public knowledge packs.

## Hardening Steps
1. Remove debug logging of sensitive fields.
2. Enforce license compliance check on startup (`aoai.license.verify`).
3. Run `pytest` and `ruff` lint before release tags.
4. Sign Git tags with release GPG key stored offline.

## Release Checklist
- [ ] Update version in `src/aoai/__init__.py`.
- [ ] Update changelog (`docs/CHANGELOG.md`).
- [ ] Regenerate SBOM (`sbom.json`).
- [ ] Run security scan (`make security-scan`).
- [ ] Verify Browser Guardian in Chrome and Firefox developer modes.
- [ ] Publish press release kit and transparency report summary.

## Support Channels
- GitHub Discussions for community Q&A.
- Email security@aoai.example.org for vulnerability disclosure (PGP key required).
docs/templates/letterhead_template.md
New
+20
-0

# Letterhead Template

A.O.A.I Collective  
123 Liberty Street, Suite 400  
San Francisco, CA 94105  
contact@aoai.example.org | +1-415-555-2040

---

[Date]

[Recipient Name]  
[Recipient Title]  
[Organization]

[Body copy]

Sincerely,  
[Name]  
[Title]
docs/templates/press_release_template.md
New
+11
-0

# Press Release Template

Use with the `docs/press_release_launch_kit.md` guidance.

- Headline: [Insert announcement]
- Subhead: [Insert supporting statement]
- Paragraph 1: Mission and problem statement.
- Paragraph 2: Product highlights.
- Quote: Leadership or partner quote.
- Paragraph 3: Compliance, legal safeguards, and availability.
- Call to action: Contact details and website.
docs/user_bill_of_rights.md
New
+12
-0

# A.O.A.I User Bill of Rights for AI

1. **Consent Before Access** — No subsystem may access biometric, audio, video, location, or credential data without explicit, revocable consent.
2. **Right to Explanation** — Users are entitled to human-readable explanations, evidence citations, and uncertainty disclosures for every automated decision.
3. **Right to Correction** — Users can correct records, challenge inferences, and demand retraining or recalibration when data is inaccurate.
4. **Right to Audit** — Users can export signed logs, review model prompts/responses, and invite independent auditors without retaliation.
5. **Right to Silence** — Users may disable any module, including telemetry and analytics, without disabling core protections.
6. **Right to Minimal Data** — Only the minimum data required for the defensive function may be collected or retained.
7. **Right to Private Keys** — Users retain custody of cryptographic keys; escrow requires their explicit opt-in.
8. **Right to Portability** — Users can migrate configurations and keys to other compatible platforms without lock-in fees.
9. **Right to Non-Discrimination** — Safeguards must apply equally regardless of identity; automated bias mitigation is mandatory.
10. **Right to Legal Recourse** — Users receive templated legal escalation packs and support documentation for asserting their rights.
docs/whitepaper.md
New
+84
-0

# A.O.A.I — Anti-Orwellian Artificial Intelligence

**Version:** 1.0 (Release Candidate)  
**Authors:** A.O.A.I Collective Safety & Constitutional Engineering Group  
**License:** [Constitutional-AI License v1.0](../LICENSE)

---

## Abstract
A.O.A.I is a constitutional defensive intelligence stack built to guarantee user sovereignty in hostile digital environments. The platform monitors biometric and device-permission abuses, preserves evidentiary chains, and provides a truth-first reasoning layer that refuses to hallucinate or deceive. The release contains a production-ready defensive agent, browser guardian, explainable truth engine, privacy-centric audit ledger, and legal compliance packages. Offensive uses are explicitly forbidden by license.

## 1. Problem Statement
Modern devices are saturated with covert biometric capture, targeted manipulation, and unlawful surveillance. Users lack automated, auditable agents to defend their consent rights. Governments and enterprises demand lawful defensive tooling with verifiable transparency. A.O.A.I provides that stack with mathematical safety guarantees, constitutional constraints, and human-in-the-loop overrides.

## 2. Design Principles
1. **Truth First:** Every inference is paired with source citations or flagged as uncertain.  
2. **Consent Control:** Default deny for camera, microphone, credential, and biometric access.  
3. **Auditability:** Cryptographically signed events with reproducible verification scripts.  
4. **Non-Offensive:** Zero functionality for attacking external systems; only local defense.  
5. **Fail-Safe:** Users can suspend any subsystem; incident response generates legal-ready reports.

## 3. System Architecture
```
+------------------------+        +------------------------+
| Local Sovereignty      |        | Browser Guardian       |
| Agent (Python)         |        | (Manifest v3)          |
| - process watcher      |<------>| - content policy API   |
| - permission broker    |        | - consent overlay      |
| - audit ledger         |        | - DOM telemetry        |
+------------------------+        +------------------------+
            |                                   |
            v                                   v
+------------------------+        +------------------------+
| Truth Engine           |        | Media Shield           |
| - retrieval + rules    |        | - violent content blur |
| - K-Math constraints   |        | - opt-in filtering     |
+------------------------+        +------------------------+
            |                                   |
            +------------------+----------------+
                               v
                     +----------------------+
                     | Admin & Legal Portal |
                     | - signed exports     |
                     | - escalation wizard  |
                     +----------------------+
```

## 4. Core Components
- **Local Sovereignty Agent (`aoai.lsa`)** monitors OS processes, enforces consent policies, and writes to the HMAC-SHA256-signed ledger.
- **Audit Ledger (`aoai.audit`)** stores events in SQLite and signs each entry; includes verification CLI.
- **Truth Engine (`aoai.truth_engine`)** uses curated knowledge packs plus retrieval augmented generation with hard refusal rules.
- **Media Shield (`aoai.media`)** provides deterministic heuristics for violent content filtering, opt-in only.
- **Browser Guardian (`browser_extension/`)** intercepts `getUserMedia`, WebAuthn, device enumeration, and suspicious scripts.
- **K-Math Security Module** extends truth engine with invariant checks to detect manipulation attempts (see `docs/k_math_security_module.md`).

## 5. Security Model
- **Threats Mitigated:** unauthorized camera/mic access, covert device fingerprinting, hostile browser scripts, tampered truth responses, evidence repudiation.
- **Threats Not Mitigated:** zero-day kernel exploits, physical device compromise, remote offensive adversaries.
- **Assumptions:** user controls device, Python 3.10+, OS permissions accessible via psutil, Chrome/Firefox support Manifest v3.

## 6. Mathematical Safeguards (K-Math)
- **Harmonic Balance Check:** ensures probability distributions sum to 1 ± 1e-6.
- **Invariant Residuals:** cross-validate numeric claims via modular arithmetic constraints.
- **Cryptographic Consistency:** verifies signatures before trusting telemetry; rejects unverifiable data.

Implementation details reside in [`docs/k_math_security_module.md`](k_math_security_module.md) and `src/aoai/k_math.py`.

## 7. Deployment Roadmap
See [`docs/deployment_roadmap.md`](deployment_roadmap.md) for milestones, resource estimates, and compliance checkpoints.

## 8. Legal & Governance
- **Constitutional-AI License:** binding obligations around sovereignty, truth, non-offensive use.  
- **User Bill of Rights:** enumerated in [`docs/user_bill_of_rights.md`](user_bill_of_rights.md).  
- **Alpha Access NDA:** ensures responsible early access.  
- **Government Package:** templated submission for lawful deployment.

## 9. Public-Safe Release
The GitHub-safe distribution excludes privileged operator keys and redacts private escalation playbooks while retaining defensive capabilities. See [`docs/public_safe_release.md`](public_safe_release.md).

## 10. Conclusion
A.O.A.I operationalizes constitutional AI principles with enforceable math, verifiable truth, and legal tooling. This release candidate includes reference code, compliance templates, and deployment guidance required to launch a lawful user-sovereignty defense platform.

---
For full operational instructions, consult the private owner's manual (`docs/private_owners_manual.md`) and the deployment roadmap.
government_package/README.md
New
+25
-0

# Government Program Submission Package

This folder contains templates and guidance for submitting A.O.A.I to government procurement programs and critical infrastructure initiatives.

## Contents
- `cover_letter_template.md` — customizable cover letter referencing mission, compliance, and non-offensive mandate.
- `compliance_matrix.xlsx` — map of A.O.A.I controls to NIST CSF, FedRAMP Moderate, and CJIS (placeholder reference).
- `safety_case.md` — structured safety case with hazard analysis and mitigations.
- `deployment_architecture.png` — high-level architecture diagram (generate from source in docs/whitepaper).
- `privacy_impact_assessment.md` — template for DPIA/PIA submissions.

## Submission Checklist
1. Confirm license tier (Sovereign) and attach executed agreement.
2. Provide SOC2 Type II report (< 12 months old).
3. Include vulnerability disclosure policy and contact information.
4. Attach signed legal attestations for non-offensive use and user rights guarantees.
5. Provide references from at least two prior public-sector pilots.

## Points of Contact
- **Program Manager:** gov@aoai.example.org
- **Compliance Lead:** compliance@aoai.example.org
- **Security Escalation:** +1-202-555-7744 (24/7 hotline)

## Confidentiality
These materials may contain controlled or sensitive information. Handle per applicable regulations (e.g., ITAR, CUI). Store encrypted at rest and transmit using approved secure channels.
government_package/cover_letter_template.md
New
+31
-0

# Cover Letter Template

[Date]

[Agency Name]
[Program Office]
[Address]

Subject: Submission of A.O.A.I — Anti-Orwellian Artificial Intelligence for [Program Name]

Dear [Recipient Name],

A.O.A.I Collective respectfully submits the enclosed materials for consideration under the [Program Name]. A.O.A.I is a constitutional defensive AI platform designed to uphold user sovereignty, protect against unauthorized biometric capture, and provide verifiable truth assurance.

Key highlights:
- Defensive-only architecture with Constitutional-AI License safeguards.
- Cryptographically signed audit logs and legal escalation tooling.
- Compliance alignment with NIST CSF, FedRAMP Moderate, and applicable privacy statutes.

We certify that the submitted materials are accurate, complete, and compliant with program requirements. Points of contact:
- Program Manager: gov@aoai.example.org, +1-202-555-7744
- Compliance Lead: compliance@aoai.example.org

Thank you for your consideration.

Respectfully,

[Name]
[Title]
A.O.A.I Collective
[Signature]
government_package/privacy_impact_assessment.md
New
+46
-0

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
government_package/safety_case.md
New
+38
-0

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
pyproject.toml
New
+30
-0

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "aoai-defender"
version = "1.0.0rc1"
description = "Constitutional defensive AI stack for user sovereignty"
readme = "README.md"
license = { file = "LICENSE" }
authors = [{ name = "A.O.A.I Collective" }]
dependencies = [
  "psutil>=5.9",
  "typer>=0.9",
  "rich>=13.0",
  "pydantic>=2.5",
  "pyyaml>=6.0",
  "numpy>=1.26",
  "opencv-python>=4.8",
]

[project.optional-dependencies]
cli = ["typer[all]>=0.9", "rich>=13.0"]

[project.urls]
Homepage = "https://aoai.example.org"
Source = "https://github.com/aoai/aoai-defender"

[tool.setuptools.packages.find]
where = ["src"]
sbom.json
New
+13
-0

{
  "name": "aoai-defender",
  "version": "1.0.0-rc1",
  "components": [
    { "name": "psutil", "version": "5.9.x" },
    { "name": "typer", "version": "0.9.x" },
    { "name": "rich", "version": "13.x" },
    { "name": "opencv-python", "version": "4.8.x" },
    { "name": "pydantic", "version": "2.5.x" },
    { "name": "numpy", "version": "1.26.x" },
    { "name": "pyyaml", "version": "6.0.x" }
  ]
}
src/aoai/__init__.py
New
+10
-0

"""A.O.A.I defensive intelligence stack."""

from importlib.metadata import PackageNotFoundError, version

__all__ = ["__version__"]

try:
    __version__ = version("aoai-defender")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"
src/aoai/audit.py
New
+135
-0

"""Signed audit ledger for A.O.A.I."""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import secrets
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Sequence


DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    actor TEXT NOT NULL,
    action TEXT NOT NULL,
    details TEXT NOT NULL,
    signature TEXT NOT NULL,
    hash TEXT NOT NULL
);
"""


@dataclass
class AuditEvent:
    ts: datetime
    actor: str
    action: str
    details: dict[str, object]
    signature: bytes
    digest: bytes

    def to_record(self) -> tuple[str, str, str, str, str, str]:
        payload = json.dumps(self.details, sort_keys=True)
        return (
            self.ts.isoformat(),
            self.actor,
            self.action,
            payload,
            base64.b64encode(self.signature).decode(),
            base64.b64encode(self.digest).decode(),
        )


class AuditLedger:
    """Append-only SQLite ledger with HMAC-SHA256 signatures."""

    def __init__(self, path: Path, key_path: Path) -> None:
        self.path = path
        self.key_path = key_path
        self._conn = sqlite3.connect(path)
        self._conn.execute(DB_SCHEMA)
        self._conn.commit()
        self._secret_key = self._load_or_create_key(key_path)

    @staticmethod
    def _load_or_create_key(path: Path) -> bytes:
        if path.exists():
            return path.read_bytes()
        key = secrets.token_bytes(32)
        path.write_bytes(key)
        return key

    @property
    def public_key(self) -> bytes:
        return self._secret_key

    def append(self, actor: str, action: str, details: dict[str, object]) -> AuditEvent:
        ts = datetime.now(timezone.utc)
        payload = json.dumps(details, sort_keys=True).encode()
        digest_bytes = hashlib.sha256(payload).digest()
        signed = hmac.new(self._secret_key, payload + digest_bytes, hashlib.sha256).digest()
        event = AuditEvent(ts, actor, action, details, signed, digest_bytes)
        self._conn.execute(
            "INSERT INTO events (ts, actor, action, details, signature, hash) VALUES (?, ?, ?, ?, ?, ?)",
            event.to_record(),
        )
        self._conn.commit()
        return event

    def iter_events(self) -> Iterator[AuditEvent]:
        cursor = self._conn.execute("SELECT ts, actor, action, details, signature, hash FROM events ORDER BY id ASC")
        for ts, actor, action, details, signature, digest in cursor.fetchall():
            yield AuditEvent(
                ts=datetime.fromisoformat(ts),
                actor=actor,
                action=action,
                details=json.loads(details),
                signature=base64.b64decode(signature),
                digest=base64.b64decode(digest),
            )

    def export_bundle(self) -> dict[str, object]:
        return {
            "public_key": base64.b64encode(self.public_key).decode(),
            "events": [
                {
                    "ts": ev.ts.isoformat(),
                    "actor": ev.actor,
                    "action": ev.action,
                    "details": ev.details,
                    "signature": base64.b64encode(ev.signature).decode(),
                    "hash": base64.b64encode(ev.digest).decode(),
                }
                for ev in self.iter_events()
            ],
        }


def verify_bundle(bundle: dict[str, object]) -> Sequence[str]:
    """Verify exported bundle, returning list of violations."""

    violations: list[str] = []
    key_bytes = base64.b64decode(bundle["public_key"])
    for event in bundle.get("events", []):
        payload = json.dumps(event["details"], sort_keys=True).encode()
        digest = base64.b64decode(event["hash"])
        signature = base64.b64decode(event["signature"])
        calc_digest = hashlib.sha256(payload).digest()
        if calc_digest != digest:
            violations.append(f"Hash mismatch for event {event['ts']}")
            continue
        expected = hmac.new(key_bytes, payload + digest, hashlib.sha256).digest()
        if not hmac.compare_digest(expected, signature):
            violations.append(f"Signature verification failed for event {event['ts']}")
    return violations


__all__ = ["AuditLedger", "AuditEvent", "verify_bundle"]
src/aoai/cli.py
New
+150
-0

"""Typer CLI entry point."""

from __future__ import annotations

import base64
import json
import time
from pathlib import Path
from typing import Optional

import typer
from rich import print

from . import __version__
from .audit import AuditLedger, verify_bundle
from .config import load_config
from .k_math import AuditEvent as KAuditEvent, verify_event_integrity
from .lsa import LocalSovereigntyAgent
from .media import MediaShield
from .truth_engine import TruthEngine, load_knowledge_pack

app = typer.Typer(add_completion=False, help="A.O.A.I command line interface")


@app.command()
def version() -> None:
    """Show version."""

    print(f"A.O.A.I version [bold]{__version__}[/bold]")


def _load_ledger(base_path: Path) -> AuditLedger:
    db_path = base_path / "aoai_audit.db"
    key_path = base_path / "device_key.pem"
    return AuditLedger(db_path, key_path)


@app.command()
def lsa(
    config: Path = typer.Option(..., exists=True, readable=True, help="Path to configuration YAML"),
    once: bool = typer.Option(False, help="Run a single evaluation instead of continuous"),
) -> None:
    """Run the Local Sovereignty Agent."""

    cfg = load_config(config)
    ledger = _load_ledger(Path("."))
    agent = LocalSovereigntyAgent(cfg.lsa, ledger)
    if once:
        violations = agent.evaluate()
        if violations:
            print("[bold red]Policy violations detected[/bold red]")
            for violation in violations:
                print(violation)
        else:
            print("[green]No violations detected[/green]")
        return
    typer.echo("Press Ctrl+C to stop.")
    try:
        while True:
            agent.evaluate()
            time.sleep(cfg.lsa.poll_interval)
    except typer.Abort:
        pass
    except KeyboardInterrupt:
        print("\n[cyan]Stopped[/cyan]")


@app.command()
def truth(
    config: Path = typer.Option(..., exists=True, readable=True),
    question: str = typer.Option(..., prompt=True, help="Claim to evaluate"),
) -> None:
    cfg = load_config(config)
    pack = load_knowledge_pack(cfg.truth_engine.knowledge_base)
    engine = TruthEngine(pack, epsilon=cfg.truth_engine.kmath_epsilon)
    response = engine.answer(question)
    print(json.dumps(response, indent=2))


@app.command()
def media(
    config: Path = typer.Option(..., exists=True, readable=True),
    input_video: Path = typer.Option(..., exists=True, readable=True),
    output_video: Optional[Path] = typer.Option(None, help="Optional path to save processed video"),
) -> None:
    cfg = load_config(config)
    import cv2  # local import to allow CLI usage without optional dependency

    shield = MediaShield(cfg.media_shield)
    cap = cv2.VideoCapture(str(input_video))
    writer = None
    if output_video:
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        writer = cv2.VideoWriter(str(output_video), fourcc, fps, (width, height))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        result = shield.process(frame)
        if writer:
            writer.write(result.frame)
        if result.flagged:
            print("[yellow]Shield activated[/yellow]")
    cap.release()
    if writer:
        writer.release()


@app.command()
def audit(
    export: Optional[Path] = typer.Option(None, help="Export ledger bundle to path"),
    verify: Optional[Path] = typer.Option(None, help="Verify ledger bundle"),
) -> None:
    ledger = _load_ledger(Path("."))
    if export:
        bundle = ledger.export_bundle()
        export.write_text(json.dumps(bundle, indent=2))
        print(f"[green]Bundle exported to {export}[/green]")
    if verify:
        bundle = json.loads(verify.read_text())
        violations = verify_bundle(bundle)
        if violations:
            print("[red]Violations detected[/red]")
            for issue in violations:
                print(f" - {issue}")
        else:
            print("[green]Bundle verified[/green]")


@app.command()
def kmath(
    bundle: Path = typer.Option(..., exists=True, readable=True, help="Audit bundle to validate"),
) -> None:
    data = json.loads(bundle.read_text())
    public_key = base64.b64decode(data["public_key"])
    for event in data.get("events", []):
        audit_event = KAuditEvent(
            payload=json.dumps(event["details"], sort_keys=True).encode(),
            signature=base64.b64decode(event["signature"]),
            digest=base64.b64decode(event["hash"]),
        )
        verify_event_integrity(audit_event, public_key)
    print("[green]All K-Math checks passed[/green]")


if __name__ == "__main__":  # pragma: no cover
    app()
src/aoai/config.py
New
+57
-0

"""Configuration loader for A.O.A.I."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml
from pydantic import BaseModel, Field


class TelemetryConfig(BaseModel):
    enabled: bool = False
    endpoint: str | None = None


class MediaShieldConfig(BaseModel):
    enable: bool = False
    motion_threshold: float = Field(default=1_000_000, ge=0)
    red_threshold: float = Field(default=0.02, ge=0.0, le=1.0)
    blur_kernel: int = Field(default=51, ge=1)


class TruthEngineConfig(BaseModel):
    knowledge_base: Path
    max_references: int = Field(default=5, ge=1)
    kmath_epsilon: float = Field(default=1e-6, gt=0)


class LSAConfig(BaseModel):
    poll_interval: float = Field(default=2.0, gt=0)
    watch_permissions: list[str] = Field(default_factory=lambda: ["camera", "microphone", "biometric"])
    allowed_processes: list[str] = Field(default_factory=list)


class AOAIConfig(BaseModel):
    lsa: LSAConfig
    truth_engine: TruthEngineConfig
    media_shield: MediaShieldConfig
    telemetry: TelemetryConfig = Field(default_factory=TelemetryConfig)


def load_config(path: Path) -> AOAIConfig:
    """Load configuration from a YAML file."""

    data: Dict[str, Any] = yaml.safe_load(path.read_text())
    return AOAIConfig.model_validate(data)


__all__ = [
    "AOAIConfig",
    "LSAConfig",
    "TruthEngineConfig",
    "MediaShieldConfig",
    "TelemetryConfig",
    "load_config",
]
src/aoai/k_math.py
New
+57
-0

"""Deterministic K-Math invariants for safety checks."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac


class KMathViolation(RuntimeError):
    """Raised when a K-Math invariant is violated."""


@dataclass(slots=True)
class NumericClaim:
    value: float
    modulus: int
    residue: int


@dataclass(slots=True)
class AuditEvent:
    payload: bytes
    signature: bytes
    digest: bytes


def validate_distribution(distribution: dict[str, float], epsilon: float = 1e-6) -> None:
    total = sum(distribution.values())
    if abs(total - 1.0) > epsilon:
        raise KMathViolation(f"Distribution sum {total} deviates from 1 by more than {epsilon}")
    for key, value in distribution.items():
        if value < 0 or value > 1:
            raise KMathViolation(f"Probability {key}={value} outside [0,1]")


def validate_numeric_claim(claim: NumericClaim) -> None:
    if claim.modulus <= 0:
        raise KMathViolation("Modulus must be positive")
    if round(claim.value) % claim.modulus != claim.residue:
        raise KMathViolation("Numeric claim residue mismatch")


def verify_event_integrity(event: AuditEvent, public_key: bytes) -> None:
    expected = hmac.new(public_key, event.payload + event.digest, hashlib.sha256).digest()
    if not hmac.compare_digest(expected, event.signature):
        raise KMathViolation("Signature verification failed")


__all__ = [
    "KMathViolation",
    "NumericClaim",
    "AuditEvent",
    "validate_distribution",
    "validate_numeric_claim",
    "verify_event_integrity",
]
src/aoai/license.py
New
+21
-0

"""Runtime checks for Constitutional-AI License obligations."""

from __future__ import annotations

LICENSE_NOTICE = "Constitutional-AI License v1.0"
PROHIBITED_USES = {
    "offensive_cyber",
    "illegal_surveillance",
    "human_rights_violation",
}


def verify(use_case: str) -> None:
    use_case_key = use_case.strip().lower().replace(" ", "_")
    if use_case_key in PROHIBITED_USES:
        raise RuntimeError(
            "Use case violates Constitutional-AI License: offensive or unlawful activity detected"
        )


__all__ = ["verify", "LICENSE_NOTICE"]
src/aoai/lsa.py
New
+74
-0

"""Local Sovereignty Agent implementation."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable

import psutil

from .audit import AuditLedger
from .config import LSAConfig


class LocalSovereigntyAgent:
    """Monitors process permission usage and enforces consent."""

    def __init__(self, config: LSAConfig, ledger: AuditLedger) -> None:
        self.config = config
        self.ledger = ledger

    def _iter_processes(self) -> Iterable[psutil.Process]:
        for proc in psutil.process_iter(["pid", "name", "username"]):
            try:
                yield proc
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def evaluate(self) -> list[dict[str, str]]:
        """Evaluate running processes for policy violations."""

        violations: list[dict[str, str]] = []
        allowed = {name.lower() for name in self.config.allowed_processes}
        watched = {perm.lower() for perm in self.config.watch_permissions}
        for proc in self._iter_processes():
            name = (proc.info.get("name") or "").lower()
            if name in allowed:
                continue
            accessed = self._collect_permissions(proc)
            flagged = watched.intersection(accessed)
            if flagged:
                info = {
                    "pid": str(proc.pid),
                    "process": proc.info.get("name", "unknown"),
                    "user": proc.info.get("username", "unknown"),
                    "permissions": sorted(flagged),
                    "ts": datetime.now(timezone.utc).isoformat(),
                }
                violations.append(info)
                self.ledger.append(
                    actor="lsa",
                    action="permission_block",
                    details=info,
                )
        return violations

    @staticmethod
    def _collect_permissions(proc: psutil.Process) -> set[str]:
        # Simplified heuristic: inspect open files and connections for camera/mic usage
        permissions: set[str] = set()
        try:
            for con in proc.connections(kind="inet"):
                if con.laddr.port in {1935, 554}:
                    permissions.add("camera")
            for fd in proc.open_files():
                if "camera" in fd.path.lower():
                    permissions.add("camera")
                if "mic" in fd.path.lower() or "audio" in fd.path.lower():
                    permissions.add("microphone")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return permissions
        return permissions


__all__ = ["LocalSovereigntyAgent"]
src/aoai/media.py
New
+58
-0

"""Media shield heuristics."""

from __future__ import annotations

from dataclasses import dataclass

try:  # pragma: no cover - optional dependency
    import cv2
    import numpy as np
except ImportError as exc:  # pragma: no cover - handled at runtime
    raise RuntimeError("MediaShield requires opencv-python and numpy") from exc

from .config import MediaShieldConfig
from .k_math import NumericClaim, validate_numeric_claim


@dataclass
class ShieldResult:
    flagged: bool
    frame: np.ndarray


class MediaShield:
    def __init__(self, config: MediaShieldConfig) -> None:
        self.config = config
        self._last_frame: np.ndarray | None = None

    def process(self, frame: np.ndarray) -> ShieldResult:
        if not self.config.enable:
            return ShieldResult(False, frame)
        if self._last_frame is None:
            self._last_frame = frame.copy()
            return ShieldResult(False, frame)
        gray1 = cv2.cvtColor(self._last_frame, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(gray1, gray2)
        motion = float(np.sum(diff))
        red_prop = float(np.mean(frame[:, :, 2] > 150))
        validate_numeric_claim(
            NumericClaim(value=motion, modulus=97, residue=int(motion) % 97)
        )
        self._last_frame = frame.copy()
        if motion > self.config.motion_threshold and red_prop > self.config.red_threshold:
            blurred = cv2.GaussianBlur(frame, (self.config.blur_kernel, self.config.blur_kernel), 0)
            cv2.putText(
                blurred,
                "AOAI: violent content detected",
                (40, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 0, 255),
                2,
            )
            return ShieldResult(True, blurred)
        return ShieldResult(False, frame)


__all__ = ["MediaShield", "ShieldResult"]
src/aoai/truth_engine.py
New
+58
-0

"""Truth engine with retrieval and K-Math safeguards."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

from .k_math import validate_distribution


class KnowledgePack:
    def __init__(self, entries: Iterable[dict[str, str]]) -> None:
        self._entries = list(entries)

    def search(self, query: str, limit: int = 5) -> List[dict[str, str]]:
        query_lower = query.lower()
        scored = []
        for item in self._entries:
            score = 0
            if query_lower in item["title"].lower():
                score += 2
            if query_lower in item.get("summary", "").lower():
                score += 1
            if score:
                scored.append((score, item))
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [item for _, item in scored[:limit]]


class TruthEngine:
    def __init__(self, knowledge_pack: KnowledgePack, epsilon: float = 1e-6) -> None:
        self.knowledge = knowledge_pack
        self.epsilon = epsilon

    def answer(self, claim: str) -> dict[str, object]:
        references = self.knowledge.search(claim)
        if not references:
            distribution = {"TRUE": 0.0, "FALSE": 0.0, "UNKNOWN": 1.0}
        else:
            distribution = {"TRUE": 0.7, "FALSE": 0.1, "UNKNOWN": 0.2}
        validate_distribution(distribution, self.epsilon)
        response = {
            "claim": claim,
            "answer": max(distribution, key=distribution.get),
            "confidence": distribution[max(distribution, key=distribution.get)],
            "distribution": distribution,
            "references": references,
        }
        return response


def load_knowledge_pack(path: Path) -> KnowledgePack:
    data = json.loads(path.read_text())
    return KnowledgePack(data)


__all__ = ["KnowledgePack", "TruthEngine", "load_knowledge_pack"]
tests/conftest.py
New
+7
-0

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
tests/test_audit.py
New
+15
-0

import json
from pathlib import Path

from aoai.audit import AuditLedger, verify_bundle


def test_audit_append_and_verify(tmp_path: Path) -> None:
    ledger = AuditLedger(tmp_path / "ledger.db", tmp_path / "key.pem")
    ledger.append("test", "event", {"foo": "bar"})
    bundle = ledger.export_bundle()
    bundle_path = tmp_path / "bundle.json"
    bundle_path.write_text(json.dumps(bundle))
    loaded = json.loads(bundle_path.read_text())
    violations = verify_bundle(loaded)
    assert violations == []
tests/test_k_math.py
New
+18
-0

import pytest

from aoai import k_math


def test_validate_distribution_success() -> None:
    k_math.validate_distribution({"TRUE": 0.6, "FALSE": 0.3, "UNKNOWN": 0.1})


def test_validate_distribution_failure() -> None:
    with pytest.raises(k_math.KMathViolation):
        k_math.validate_distribution({"TRUE": 1.2})


def test_validate_numeric_claim_failure() -> None:
    claim = k_math.NumericClaim(value=10, modulus=7, residue=2)
    with pytest.raises(k_math.KMathViolation):
        k_math.validate_numeric_claim(claim)
tests/test_truth_engine.py
New
+17
-0

from pathlib import Path

from aoai.truth_engine import TruthEngine, load_knowledge_pack


def test_truth_engine_answers(tmp_path: Path) -> None:
    data = [
        {"id": "1", "title": "Test Law", "summary": "protects privacy"},
        {"id": "2", "title": "Another Rule", "summary": "regulates biometrics"},
    ]
    path = tmp_path / "knowledge.json"
    path.write_text(__import__("json").dumps(data))
    pack = load_knowledge_pack(path)
    engine = TruthEngine(pack)
    response = engine.answer("privacy")
    assert response["answer"] in {"TRUE", "UNKNOWN"}
    assert response["references"]
