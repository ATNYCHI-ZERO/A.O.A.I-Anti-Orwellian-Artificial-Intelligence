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
