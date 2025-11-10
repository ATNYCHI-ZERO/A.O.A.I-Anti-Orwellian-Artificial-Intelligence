"""Typer CLI entry point."""

from __future__ import annotations

import base64
import json
from pathlib import Path
from typing import Optional

import typer
from rich import print
import time

from . import __version__
from .audit import AuditLedger, verify_bundle
from .config import load_config
from .k_math import AuditEvent as KAuditEvent, verify_event_integrity
from .lsa import LocalSovereigntyAgent
from .media import MediaShield
from .truth_engine import TruthEngine, load_knowledge_pack

app = typer.Typer(add_completion=False, help="A.O.A.I command line interface")


@app.command()
def version() -> None:
    """Show version."""

    print(f"A.O.A.I version [bold]{__version__}[/bold]")


def _load_ledger(base_path: Path) -> AuditLedger:
    db_path = base_path / "aoai_audit.db"
    key_path = base_path / "device_key.pem"
    return AuditLedger(db_path, key_path)


@app.command()
def lsa(
    config: Path = typer.Option(..., exists=True, readable=True, help="Path to configuration YAML"),
    once: bool = typer.Option(False, help="Run a single evaluation instead of continuous"),
) -> None:
    """Run the Local Sovereignty Agent."""

    cfg = load_config(config)
    ledger = _load_ledger(Path("."))
    agent = LocalSovereigntyAgent(cfg.lsa, ledger)
    if once:
        violations = agent.evaluate()
        if violations:
            print("[bold red]Policy violations detected[/bold red]")
            for violation in violations:
                print(violation)
        else:
            print("[green]No violations detected[/green]")
        return
    typer.echo("Press Ctrl+C to stop.")
    try:
        while True:
            agent.evaluate()
            time.sleep(cfg.lsa.poll_interval)
    except typer.Abort:
        pass
    except KeyboardInterrupt:
        print("\n[cyan]Stopped[/cyan]")


@app.command()
def truth(
    config: Path = typer.Option(..., exists=True, readable=True),
    question: str = typer.Option(..., prompt=True, help="Claim to evaluate"),
) -> None:
    cfg = load_config(config)
    pack = load_knowledge_pack(cfg.truth_engine.knowledge_base)
    engine = TruthEngine(pack, epsilon=cfg.truth_engine.kmath_epsilon)
    response = engine.answer(question)
    print(json.dumps(response, indent=2))


@app.command()
def media(
    config: Path = typer.Option(..., exists=True, readable=True),
    input_video: Path = typer.Option(..., exists=True, readable=True),
    output_video: Optional[Path] = typer.Option(None, help="Optional path to save processed video"),
) -> None:
    cfg = load_config(config)
    import cv2  # local import to allow CLI usage without optional dependency

    shield = MediaShield(cfg.media_shield)
    cap = cv2.VideoCapture(str(input_video))
    writer = None
    if output_video:
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        writer = cv2.VideoWriter(str(output_video), fourcc, fps, (width, height))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        result = shield.process(frame)
        if writer:
            writer.write(result.frame)
        if result.flagged:
            print("[yellow]Shield activated[/yellow]")
    cap.release()
    if writer:
        writer.release()


@app.command()
def audit(
    export: Optional[Path] = typer.Option(None, help="Export ledger bundle to path"),
    verify: Optional[Path] = typer.Option(None, help="Verify ledger bundle"),
) -> None:
    ledger = _load_ledger(Path("."))
    if export:
        bundle = ledger.export_bundle()
        export.write_text(json.dumps(bundle, indent=2))
        print(f"[green]Bundle exported to {export}[/green]")
    if verify:
        bundle = json.loads(verify.read_text())
        violations = verify_bundle(bundle)
        if violations:
            print("[red]Violations detected[/red]")
            for issue in violations:
                print(f" - {issue}")
        else:
            print("[green]Bundle verified[/green]")


@app.command()
def kmath(
    bundle: Path = typer.Option(..., exists=True, readable=True, help="Audit bundle to validate"),
) -> None:
    data = json.loads(bundle.read_text())
    public_key = base64.b64decode(data["public_key"])
    for event in data.get("events", []):
        audit_event = KAuditEvent(
            payload=json.dumps(event["details"], sort_keys=True).encode(),
            signature=base64.b64decode(event["signature"]),
            digest=base64.b64decode(event["hash"]),
        )
        verify_event_integrity(audit_event, public_key)
    print("[green]All K-Math checks passed[/green]")


if __name__ == "__main__":  # pragma: no cover
    app()
