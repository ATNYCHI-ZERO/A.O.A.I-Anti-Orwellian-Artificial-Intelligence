 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/browser_extension/README.md b/browser_extension/README.md
new file mode 100644
index 0000000000000000000000000000000000000000..a5f829ca036bca34f4c12397dff4ac2c4bd1a5c5
--- /dev/null
+++ b/browser_extension/README.md
@@ -0,0 +1,15 @@
+# A.O.A.I Browser Guardian
+
+## Overview
+Manifest v3 extension that blocks unauthorized media access, captures consent events, and syncs with the Local Sovereignty Agent.
+
+## Installation
+1. Open browser extensions page (Chrome: `chrome://extensions`, Firefox: `about:debugging#/runtime/this-firefox`).
+2. Enable developer mode.
+3. Click "Load unpacked" and select this folder.
+4. Pin the extension to quickly toggle consent.
+
+## Usage
+- Use the popup to grant or revoke camera/microphone consent; the setting propagates to all active tabs.
+- Review the last 10 events in the popup log.
+- Events are stored in `chrome.storage.local` and mirrored to the Local Sovereignty Agent via native messaging (see CLI documentation).
 
EOF
)
