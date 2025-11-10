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
