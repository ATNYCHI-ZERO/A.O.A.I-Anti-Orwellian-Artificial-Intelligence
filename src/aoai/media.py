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
