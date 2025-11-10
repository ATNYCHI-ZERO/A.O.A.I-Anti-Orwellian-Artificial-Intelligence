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
