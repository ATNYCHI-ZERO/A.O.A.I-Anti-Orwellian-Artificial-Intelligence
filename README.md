# A.O.A.I — Anti-Orwellian Artificial Intelligence

A.O.A.I is an educational reference project that explores how privacy-first guardrails can be layered on top of small, auditable AI workflows. The repository combines a lightweight Python stack for local policy enforcement with supporting collateral (policies, governance templates, and a demo browser extension) so the full release kit lives in one place.

> **Note**
> None of the code or documents in this repository should be treated as production-ready legal advice or deployed to protect real users without a thorough security review. The goal is to illustrate defensive patterns, not to provide drop-in compliance tooling.

## Key components

- **Local Sovereignty Agent (LSA)** – Watches for disallowed permissions or processes according to a YAML configuration and writes tamper-evident audit records. (See `src/aoai/lsa.py` and `src/aoai/audit.py`.)
- **Truth Engine** – Loads a compact "knowledge pack" and scores claims with simple lexical checks to demonstrate transparent fact evaluation. (See `src/aoai/truth_engine.py`.)
- **Media Shield** – Applies quick video heuristics (motion/redness/blur) to flag frames that might need human review. (See `src/aoai/media.py`.)
- **Typer CLI** – Entry point that ties the subsystems together for demos and testing. (See `src/aoai/cli.py`.)
- **Browser Guardian extension** – Manifest v3 example that surfaces permission prompts and relays signed events to the audit ledger. (See `browser_extension/`.)
- **Governance bundle** – Whitepaper, bill of rights, licensing drafts, investor one-pager, and other narrative assets under `docs/` and `government_package/` for teams exploring responsible launch messaging.

## Quickstart

1. **Clone and enter the repository**
   ```bash
   git clone https://github.com/example/A.O.A.I-Anti-Orwellian-Artificial-Intelligence.git
   cd A.O.A.I-Anti-Orwellian-Artificial-Intelligence
   ```
2. **Provision a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .
   pip install -e .[cli]  # optional extras for richer CLI output
   ```
   The optional `[cli]` extras enable Typer's rich help output for the command line interface.
3. **Run the smoke test suite**
   ```bash
   pytest
   ```
4. **Launch a demo workflow**
   ```bash
   python -m aoai.cli lsa --config configs/demo.yaml --once
   ```
   This executes the Local Sovereignty Agent once and prints any policy violations detected on your machine.

## Repository layout

```
.
├── configs/                 # Example YAML configuration files
├── data/                    # Demo knowledge base JSON files
├── src/aoai/                # Python package implementing the defensive stack
├── browser_extension/       # Consent-forwarding demo extension
├── docs/                    # Policy, licensing, and rollout documents
├── government_package/      # Government-focused submission templates
├── tests/                   # Unit tests covering core modules
└── assets/                  # Logos and brand references
```

## Requirements

- Python 3.10 or newer
- Optional: OpenCV (`pip install opencv-python`) if you plan to run the media shield command
- A virtual environment is strongly recommended for local development

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

The editable install registers the `aoai` package and exposes the CLI as `python -m aoai.cli`. Install the optional `[cli]` extras if you want Typer's formatted help screens. Each CLI command supports `--help` for detailed arguments and flags.

## Usage

### Check the installed version
```bash
python -m aoai.cli version
```

### Run the Local Sovereignty Agent once
```bash
python -m aoai.cli lsa --config configs/demo.yaml --once
```
This evaluates the configured policies a single time and reports any violations.

### Continuous monitoring
```bash
python -m aoai.cli lsa --config configs/demo.yaml
```
Press <kbd>Ctrl</kbd>+<kbd>C</kbd> to stop the loop.

### Ask the truth engine a question
```bash
python -m aoai.cli truth --config configs/demo.yaml --question "What is the surveillance policy?"
```
The response includes a confidence score and the references pulled from the knowledge pack JSON file.

### Process a video sample *(requires OpenCV)*
```bash
python -m aoai.cli media --config configs/demo.yaml --input-video path/to/input.mp4 --output-video shielded.mp4
```
Frames that trip a heuristic are logged to stdout and, when an output path is supplied, written to the processed file.

### Export and verify audit bundles
```bash
python -m aoai.cli audit --export bundle.json
python -m aoai.cli audit --verify bundle.json
python -m aoai.cli kmath --bundle bundle.json  # extra integrity check
```
Audit exports include a public key, hashed events, and signatures so the bundle can be verified on another machine.

### Generate a release package
```bash
python -m build
```
The project is configured with PEP 517 metadata in `pyproject.toml`. Running the command above produces wheel and source distributions inside the `dist/` folder for downstream packaging experiments.

### Lint and format the codebase
```bash
pip install ruff
ruff check src tests
ruff format src tests
```
Use these helpers before submitting pull requests to keep the repository consistent.

## Configuration

All CLI commands share a YAML configuration file. The example at `configs/demo.yaml` shows the expected structure:

- `lsa` – Poll interval (seconds), permissions to watch, and allowed process names.
- `truth_engine` – Path to a knowledge pack JSON file, maximum reference count, and epsilon for K-Math integrity checks.
- `media_shield` – Toggle, motion and color thresholds, and Gaussian blur kernel size.
- `telemetry` – Placeholder options demonstrating how remote reporting could be configured.

Adjust the values to experiment with tighter or looser policies. The pydantic models in `src/aoai/config.py` validate the configuration at load time.

## Browser extension

The sample extension under `browser_extension/` can be loaded as an unpacked extension in Chromium-based browsers or Firefox Developer Edition. It intercepts permission prompts, forwards consent events, and illustrates how the audit ledger might receive signed updates from a user interface surface.

1. Open your browser's extensions page (e.g., `chrome://extensions/`).
2. Enable **Developer mode**.
3. Choose **Load unpacked** and select the `browser_extension/` directory.
4. Interact with pages that request camera, microphone, or location permissions—the extension logs consent events and forwards them to the local audit ledger endpoint defined in `configs/demo.yaml`.

> Tip: Update the `browser_extension/manifest.json` `externally_connectable` URLs to match your local testing domain before sharing the build with collaborators.

## Tests and quality checks

- **Unit tests**
  ```bash
  pytest
  ```
- **Static analysis** (optional)
  ```bash
  pip install ruff
  ruff check src tests
  ```
- **Type checks**
  ```bash
  pip install pyright
  pyright
  ```

The tests cover the audit ledger, K-Math verification helpers, and truth engine scoring. Static and type analysis reinforce those checks by highlighting dead code paths or mismatched interfaces before runtime.

## Contributing

Pull requests and issue reports are welcome. Please review `CONTRIBUTING.md` for coding standards and submission guidelines.

When opening a pull request, consider including:

- A summary of the user-facing change
- Screenshots or terminal captures for CLI or UI updates
- A checklist of tests you ran locally (`pytest`, `ruff`, `pyright`, etc.)

Large or breaking changes should begin as an issue thread so we can scope the work together before implementation.

## License and governance resources

This project is published under the [Constitutional-AI License v1.0](LICENSE). See `docs/commercial_license_tiers.md` for commercial terms and the `government_package/` directory for compliance templates.

Additional governance documents you may find useful:

- `docs/user_bill_of_rights.md` – Suggested user protections when operating the stack
- `docs/deployment_roadmap.md` – Suggested sequence for safe pilots through public launch
- `docs/press_release_launch_kit.md` – Communication checklist for external announcements
- `docs/private_owners_manual.md` – Internal operating notes covering overrides and emergency stops

Refer to `docs/` for the full release kit, including the whitepaper, investor one-pager, and trademark assets.
