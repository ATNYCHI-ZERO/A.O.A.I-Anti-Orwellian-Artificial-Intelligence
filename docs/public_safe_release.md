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
