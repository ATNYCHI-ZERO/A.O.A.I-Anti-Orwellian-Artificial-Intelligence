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
