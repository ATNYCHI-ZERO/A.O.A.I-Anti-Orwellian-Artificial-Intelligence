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
