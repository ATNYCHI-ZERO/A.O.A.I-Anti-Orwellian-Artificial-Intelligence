"""Local Sovereignty Agent implementation."""

from __future__ import annotations

import psutil
from datetime import datetime, timezone
from typing import Iterable

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
