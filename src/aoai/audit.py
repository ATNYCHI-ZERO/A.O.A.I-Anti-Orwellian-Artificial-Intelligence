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
