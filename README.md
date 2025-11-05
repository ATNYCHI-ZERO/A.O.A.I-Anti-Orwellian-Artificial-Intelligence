
 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index 9e809027c547d778b8bb884040bcf4a6b0190160..641fded337d7eb1c933513ed86c95d8530306099 100644
--- a/README.md
+++ b/README.md
@@ -1,305 +1,189 @@
-# A.O.A.I-Anti-Orwellian-Artificial-Intelligence
-White Paper v0.9 — Lawful Defensive Build
+# A.O.A.I — Anti-Orwellian Artificial Intelligence
+
+A.O.A.I is an educational reference project that explores how privacy-first guardrails can be layered on top of small, auditable AI workflows. The repository combines a lightweight Python stack for local policy enforcement with supporting collateral (policies, governance templates, and a demo browser extension) so the full release kit lives in one place.
+
+> **Note**
+> None of the code or documents in this repository should be treated as production-ready legal advice or deployed to protect real users without a thorough security review. The goal is to illustrate defensive patterns, not to provide drop-in compliance tooling.
+
+## Key components
+
+- **Local Sovereignty Agent (LSA)** – Watches for disallowed permissions or processes according to a YAML configuration and writes tamper-evident audit records. (See `src/aoai/lsa.py` and `src/aoai/audit.py`.)
+- **Truth Engine** – Loads a compact "knowledge pack" and scores claims with simple lexical checks to demonstrate transparent fact evaluation. (See `src/aoai/truth_engine.py`.)
+- **Media Shield** – Applies quick video heuristics (motion/redness/blur) to flag frames that might need human review. (See `src/aoai/media.py`.)
+- **Typer CLI** – Entry point that ties the subsystems together for demos and testing. (See `src/aoai/cli.py`.)
+- **Browser Guardian extension** – Manifest v3 example that surfaces permission prompts and relays signed events to the audit ledger. (See `browser_extension/`.)
+- **Governance bundle** – Whitepaper, bill of rights, licensing drafts, investor one-pager, and other narrative assets under `docs/` and `government_package/` for teams exploring responsible launch messaging.
+
+## Quickstart
+
+1. **Clone and enter the repository**
+   ```bash
+   git clone https://github.com/example/A.O.A.I-Anti-Orwellian-Artificial-Intelligence.git
+   cd A.O.A.I-Anti-Orwellian-Artificial-Intelligence
+   ```
+2. **Provision a virtual environment and install dependencies**
+   ```bash
+   python -m venv .venv
+   source .venv/bin/activate
+   pip install -e .
+   pip install -e .[cli]  # optional extras for richer CLI output
+   ```
+   The optional `[cli]` extras enable Typer's rich help output for the command line interface.
+3. **Run the smoke test suite**
+   ```bash
+   pytest
+   ```
+4. **Launch a demo workflow**
+   ```bash
+   python -m aoai.cli lsa --config configs/demo.yaml --once
+   ```
+   This executes the Local Sovereignty Agent once and prints any policy violations detected on your machine.
+
+## Repository layout
+
+```
+.
+├── configs/                 # Example YAML configuration files
+├── data/                    # Demo knowledge base JSON files
+├── src/aoai/                # Python package implementing the defensive stack
+├── browser_extension/       # Consent-forwarding demo extension
+├── docs/                    # Policy, licensing, and rollout documents
+├── government_package/      # Government-focused submission templates
+├── tests/                   # Unit tests covering core modules
+└── assets/                  # Logos and brand references
+```
+
+## Requirements
+
+- Python 3.10 or newer
+- Optional: OpenCV (`pip install opencv-python`) if you plan to run the media shield command
+- A virtual environment is strongly recommended for local development
+
+## Installation
+
+```bash
+python -m venv .venv
+source .venv/bin/activate
+pip install -e .
+```
+
+The editable install registers the `aoai` package and exposes the CLI as `python -m aoai.cli`. Install the optional `[cli]` extras if you want Typer's formatted help screens. Each CLI command supports `--help` for detailed arguments and flags.
+
+## Usage
+
+### Check the installed version
+```bash
+python -m aoai.cli version
+```
+
+### Run the Local Sovereignty Agent once
+```bash
+python -m aoai.cli lsa --config configs/demo.yaml --once
+```
+This evaluates the configured policies a single time and reports any violations.
+
+### Continuous monitoring
+```bash
+python -m aoai.cli lsa --config configs/demo.yaml
+```
+Press <kbd>Ctrl</kbd>+<kbd>C</kbd> to stop the loop.
+
+### Ask the truth engine a question
+```bash
+python -m aoai.cli truth --config configs/demo.yaml --question "What is the surveillance policy?"
+```
+The response includes a confidence score and the references pulled from the knowledge pack JSON file.
+
+### Process a video sample *(requires OpenCV)*
+```bash
+python -m aoai.cli media --config configs/demo.yaml --input-video path/to/input.mp4 --output-video shielded.mp4
+```
+Frames that trip a heuristic are logged to stdout and, when an output path is supplied, written to the processed file.
+
+### Export and verify audit bundles
+```bash
+python -m aoai.cli audit --export bundle.json
+python -m aoai.cli audit --verify bundle.json
+python -m aoai.cli kmath --bundle bundle.json  # extra integrity check
+```
+Audit exports include a public key, hashed events, and signatures so the bundle can be verified on another machine.
+
+### Generate a release package
+```bash
+python -m build
+```
+The project is configured with PEP 517 metadata in `pyproject.toml`. Running the command above produces wheel and source distributions inside the `dist/` folder for downstream packaging experiments.
+
+### Lint and format the codebase
+```bash
+pip install ruff
+ruff check src tests
+ruff format src tests
+```
+Use these helpers before submitting pull requests to keep the repository consistent.
+
+## Configuration
+
+All CLI commands share a YAML configuration file. The example at `configs/demo.yaml` shows the expected structure:
+
+- `lsa` – Poll interval (seconds), permissions to watch, and allowed process names.
+- `truth_engine` – Path to a knowledge pack JSON file, maximum reference count, and epsilon for K-Math integrity checks.
+- `media_shield` – Toggle, motion and color thresholds, and Gaussian blur kernel size.
+- `telemetry` – Placeholder options demonstrating how remote reporting could be configured.
+
+Adjust the values to experiment with tighter or looser policies. The pydantic models in `src/aoai/config.py` validate the configuration at load time.
+
+## Browser extension
+
+The sample extension under `browser_extension/` can be loaded as an unpacked extension in Chromium-based browsers or Firefox Developer Edition. It intercepts permission prompts, forwards consent events, and illustrates how the audit ledger might receive signed updates from a user interface surface.
 
-1. Executive summary
+1. Open your browser's extensions page (e.g., `chrome://extensions/`).
+2. Enable **Developer mode**.
+3. Choose **Load unpacked** and select the `browser_extension/` directory.
+4. Interact with pages that request camera, microphone, or location permissions—the extension logs consent events and forwards them to the local audit ledger endpoint defined in `configs/demo.yaml`.
+
+> Tip: Update the `browser_extension/manifest.json` `externally_connectable` URLs to match your local testing domain before sharing the build with collaborators.
+
+## Tests and quality checks
 
-A.O.A.I is a user-sovereignty agent.
-It enforces truth-first behaviour, refuses to deceive, minimizes data collection, and defends the user device from unauthorized biometric scans and covert profiling.
-It does not attack or disable external systems. It detects, blocks local vectors, logs, and escalates legally.
+- **Unit tests**
+  ```bash
+  pytest
+  ```
+- **Static analysis** (optional)
+  ```bash
+  pip install ruff
+  ruff check src tests
+  ```
+- **Type checks**
+  ```bash
+  pip install pyright
+  pyright
+  ```
 
-2. Mission & principles
+The tests cover the audit ledger, K-Math verification helpers, and truth engine scoring. Static and type analysis reinforce those checks by highlighting dead code paths or mismatched interfaces before runtime.
 
-Truth-first. If uncertain, report uncertainty.
+## Contributing
 
-Consent as default. No data access without explicit grant.
+Pull requests and issue reports are welcome. Please review `CONTRIBUTING.md` for coding standards and submission guidelines.
 
-Privacy by design. Local-first, end-to-end encryption for remote telemetry.
+When opening a pull request, consider including:
 
-Auditability. Immutable, signed logs.
+- A summary of the user-facing change
+- Screenshots or terminal captures for CLI or UI updates
+- A checklist of tests you ran locally (`pytest`, `ruff`, `pyright`, etc.)
 
-Non-offensive. No capability to attack external systems.
+Large or breaking changes should begin as an issue thread so we can scope the work together before implementation.
 
-Fail-safe. User control, clear opt-out.
+## License and governance resources
 
-3. System goals
+This project is published under the [Constitutional-AI License v1.0](LICENSE). See `docs/commercial_license_tiers.md` for commercial terms and the `government_package/` directory for compliance templates.
 
-Detect unauthorized biometric/face/ID scans or model probing of a user device.
+Additional governance documents you may find useful:
 
-Block or deny local requests for camera/mic/credential access when consent absent.
+- `docs/user_bill_of_rights.md` – Suggested user protections when operating the stack
+- `docs/deployment_roadmap.md` – Suggested sequence for safe pilots through public launch
+- `docs/press_release_launch_kit.md` – Communication checklist for external announcements
+- `docs/private_owners_manual.md` – Internal operating notes covering overrides and emergency stops
 
-Detect violent media streams and offer automatic local shielding.
-
-Provide cryptographically signed audit trails for legal escalation.
-
-Provide an explainable truth engine that references verifiable sources.
-
-4. Architecture overview
-
-Components:
-
-Local Sovereignty Agent (LSA) — runs on user device. Monitors processes, network connections, permission usages, browser APIs. Blocks local access when unauthorized.
-
-Browser Guardian — extension that intercepts getUserMedia, WebAuthn, camera/microphone permission usage and monitors DOM scripts for fingerprinting behavior.
-
-Truth Engine — a model+ruleset that evaluates factual claims against verifiable sources. Returns TRUE / FALSE / UNKNOWN + evidence links.
-
-Privacy Kernel — manages keys, zero-knowledge proof components, and local encryption.
-
-Audit Ledger — sqlite + ed25519 signed append-only log for every access event.
-
-Admin Console / Incident Workflow — alerting, legal escalation package builder, exportable signed evidence bundle.
-
-5. Threat model (allowed defensive scope)
-
-Allowed to detect and block:
-
-Local programs attempting to access camera/microphone without user consent.
-
-Browser scripts trying to intercept getUserMedia or enumerate devices covertly.
-
-Local processes attempting to scrape files that match PII patterns.
-
-Network attempts to fingerprint device or exfiltrate biometric payloads.
-
-Not allowed:
-
-Remote offensive actions (DDoS, jamming, disabling other servers).
-
-Interfering with third-party infrastructure or law-enforcement systems.
-
-6. Detection strategies (high level)
-
-Permission monitoring: watch OS and browser permission APIs. Deny by default.
-
-Process heuristic signatures: whitelist known apps. Flag unknown processes that query camera/USB/TPM.
-
-Network fingerprint detection: detect scanning patterns, model probing (repeated inference queries).
-
-Behavioral ML: classify scripts attempting to load face-recognition models or WASM inference engines.
-
-Media content shield: frame-level heuristics to detect likely violent/graphic content. Automatically blur or pause locally.
-
-K-Math resonance constraints: use deterministic invariants to check internal model consistency (described below as verification constraints).
-
-7. Truth engine (concept)
-
-Use a small verifiable knowledge layer. For claims, fetch primary sources, compute structural matches, and only return "TRUE" when matched to authoritative source(s). Otherwise return "UNKNOWN" or "DISPUTED".
-
-K-Math harmonic constraints implemented as deterministic consistency checks. These are formal invariants applied to numeric/cryptographic claims. (This is a design pattern. Implementation requires specifying the K-Math operators you use.)
-
-8. Audit & evidentiary package
-
-All events signed with device key (Ed25519).
-
-Export format: signed JSONL + compressed evidence (network capture, screenshots, process metadata).
-
-For legal use, include chain of custody notes, timestamps in UTC, and verification script.
-
-Proof-of-Concept Code (defensive only)
-
-Below are minimal PoC components. They run on the user device and in the browser. They are intentionally limited to non-offensive defensive actions.
-
-Requirements: Python 3.10+, psutil, cryptography, flask (for demo UI), opencv-python (optional for media shield). Browser extension is manifest v3.
-
-1) Local Sovereignty Agent — monitor local camera/mic access & sign events
-# aoai_lsa.py  -- defensive-only PoC
-import time, json, sqlite3, os
-from datetime import datetime, timezone
-import psutil
-from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
-from cryptography.hazmat.primitives import serialization
-
-DB = "aoai_audit.db"
-KEYFILE = "device_key.pem"
-WATCH_PIDS = set()
-UNWANTED_SIGNATURES = ["covert_cam", "face_scrape", "id_probe"]  # heuristics
-
-def init_db():
-    if not os.path.exists(DB):
-        conn = sqlite3.connect(DB)
-        conn.execute("""CREATE TABLE audit (ts TEXT, event TEXT, meta TEXT, sig BLOB)""")
-        conn.commit()
-        conn.close()
-
-def load_or_create_key():
-    if os.path.exists(KEYFILE):
-        sk = Ed25519PrivateKey.from_private_bytes(open(KEYFILE,"rb").read())
-        return sk
-    sk = Ed25519PrivateKey.generate()
-    open(KEYFILE,"wb").write(sk.private_bytes(
-        encoding=serialization.Encoding.Raw,
-        format=serialization.PrivateFormat.Raw,
-        encryption_algorithm=serialization.NoEncryption()))
-    return sk
-
-def sign_and_store(sk, event, meta):
-    ts = datetime.now(timezone.utc).isoformat()
-    blob = json.dumps({"ts": ts, "event": event, "meta": meta}, separators=(",",":")).encode()
-    sig = sk.sign(blob)
-    conn = sqlite3.connect(DB)
-    conn.execute("INSERT INTO audit VALUES (?,?,?,?)", (ts, event, json.dumps(meta), sig))
-    conn.commit()
-    conn.close()
-    print("AUDIT:", event, meta)
-
-def scan_processes(sk):
-    for p in psutil.process_iter(['pid','name','cmdline','username']):
-        try:
-            name = (p.info['name'] or "").lower()
-            cmd = " ".join(p.info.get('cmdline') or [])
-        except Exception:
-            continue
-        if any(s in name for s in UNWANTED_SIGNATURES) or any(s in cmd.lower() for s in UNWANTED_SIGNATURES):
-            meta = {"pid": p.info['pid'], "name": p.info['name'], "cmdline": p.info.get('cmdline')}
-            sign_and_store(sk, "unauthorized_local_access_attempt", meta)
-            # Defensive-local-only action: suspend or alert
-            try:
-                p.suspend()
-                sign_and_store(sk, "suspended_process_local", {"pid": p.info['pid']})
-            except Exception as e:
-                sign_and_store(sk, "suspend_failed", {"pid": p.info['pid'], "error": str(e)})
-
-if __name__ == "__main__":
-    init_db()
-    sk = load_or_create_key()
-    while True:
-        scan_processes(sk)
-        time.sleep(2)
-
-
-Notes:
-
-This suspends only local processes. It is defensive and legal on devices you own.
-
-Replace heuristics with robust allowlist/denylist per organizational policy.
-
-2) Browser Guardian — manifest + content script (intercepts camera usage)
-
-manifest.json (v3 minimal)
-
-{
-  "manifest_version": 3,
-  "name": "AOAI Guardian",
-  "version": "0.1",
-  "permissions": ["tabs","scripting","storage"],
-  "host_permissions": ["<all_urls>"],
-  "background": {"service_worker": "bg.js"},
-  "content_scripts": [{
-    "matches": ["<all_urls>"],
-    "js": ["content.js"],
-    "run_at": "document_start"
-  }]
-}
-
-
-content.js
-
-// intercept getUserMedia and enumerateDevices
-(function(){
-  const origGet = navigator.mediaDevices && navigator.mediaDevices.getUserMedia;
-  if (!origGet) return;
-  navigator.mediaDevices.getUserMedia = function(constraints){
-    // block by default unless user explicitly grants via extension UI
-    const allowed = localStorage.getItem("aoai_allow_media") === "true";
-    if (!allowed) {
-      console.warn("AOAI: blocked getUserMedia (consent missing)");
-      // send a browser event to background for logging
-      window.postMessage({aoai_event: "blocked_getUserMedia", constraints}, "*");
-      return Promise.reject(new Error("AOAI: media access blocked (consent required)"));
-    }
-    return origGet.call(this, constraints);
-  };
-})();
-
-
-Background worker bg.js would listen for postMessages and log.
-
-3) Media Shield — simple violent-content heuristic (frame motion + color / face collision)
-
-This is a heuristic to blur frames when motion intensity and redness (blood proxies) exceed threshold. It is NOT a replacement for an ML classifier but is conservative.
-
-# media_shield.py
-import cv2, numpy as np
-
-def detect_violation(frame, last_frame):
-    if last_frame is None:
-        return False, frame
-    gray1 = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
-    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
-    diff = cv2.absdiff(gray1, gray2)
-    motion = np.sum(diff)/255.0
-    # estimate "red" proportion
-    red_prop = np.mean(frame[:,:,2] > 150)
-    if motion > 1e6 and red_prop > 0.02:  # heuristic thresholds
-        # blur and warn
-        blurred = cv2.GaussianBlur(frame, (51,51), 0)
-        return True, blurred
-    return False, frame
-
-cap = cv2.VideoCapture("input.mp4")
-last = None
-out = None
-while True:
-    ret, frame = cap.read()
-    if not ret: break
-    flag, out_frame = detect_violation(frame, last)
-    last = frame.copy()
-    if flag:
-        # show overlay
-        cv2.putText(out_frame, "AOAI: violent content detected", (50,50),
-                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
-    cv2.imshow("shield", out_frame)
-    if cv2.waitKey(1) & 0xFF == ord('q'):
-        break
-cap.release()
-cv2.destroyAllWindows()
-
-
-User opt-in required before taking automatic actions.
-
-4) Cryptographic audit example (sign and verify)
-from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
-from cryptography.hazmat.primitives import serialization
-import json, base64
-
-# sign
-sk = Ed25519PrivateKey.generate()
-msg = json.dumps({"ts":"2025-11-04T00:00:00Z","event":"blocked_getUserMedia"}).encode()
-sig = sk.sign(msg)
-
-# export public key for verification
-pk = sk.public_key()
-pub_bytes = pk.public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
-print("pubkey:", base64.b64encode(pub_bytes).decode(), "sig:", base64.b64encode(sig).decode())
-
-Governance, legal, and operations
-
-Governance Board: mixed user-elected + independent experts. Public charter.
-
-Open audits: signed model behavior logs. Third-party auditing required.
-
-Escalation: build a legal escalation pack template that users can send to counsel, CISA, or law enforcement. Include signed evidence, hashes, and metadata.
-
-Deployment options & roadmap
-
-MVP (0–3 months): Local LSA + browser guardian + basic audit log.
-
-Phase 2 (3–9 months): Truth engine with curated source index. User UI. Legal pack builder.
-
-Phase 3 (9–18 months): Enterprise integrations (MFA, EDR compatibility), hardened hardware enclave option.
-
-Refusal to include offensive language or offers
-
-I will not encode or deliver a message that offers to attack, disable, jam, or illegally interfere with other systems. I will not add a line that says “if you need one that attacks/do disables I can and will go offline.” That would encourage criminal behavior. If you want to communicate with a funder or partner, use lawful language. Example safe pitch you may include to a partner:
-
-“If you want aggressive, legally compliant defensive capabilities, A.O.A.I can provide on-device active defense, hardened enclaves, and coordinated incident response. For any offensive or enforcement needs we will only proceed through proper legal channels and accredited red teams under contract.”
-
-Legal & ethics note (short)
-
-Offensive cyber actions are illegal in most jurisdictions.
-
-A.O.A.I must be transparent and auditable.
-
-Build with counsel and a certified security team.
-
-Maintain user consent logs for every defensive action.
+Refer to `docs/` for the full release kit, including the whitepaper, investor one-pager, and trademark assets.
 
EOF
)
