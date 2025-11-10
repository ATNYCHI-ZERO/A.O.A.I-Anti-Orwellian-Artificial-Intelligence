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
