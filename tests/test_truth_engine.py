from pathlib import Path

from aoai.truth_engine import TruthEngine, load_knowledge_pack


def test_truth_engine_answers(tmp_path: Path) -> None:
    data = [
        {"id": "1", "title": "Test Law", "summary": "protects privacy"},
        {"id": "2", "title": "Another Rule", "summary": "regulates biometrics"},
    ]
    path = tmp_path / "knowledge.json"
    path.write_text(__import__("json").dumps(data))
    pack = load_knowledge_pack(path)
    engine = TruthEngine(pack)
    response = engine.answer("privacy")
    assert response["answer"] in {"TRUE", "UNKNOWN"}
    assert response["references"]
