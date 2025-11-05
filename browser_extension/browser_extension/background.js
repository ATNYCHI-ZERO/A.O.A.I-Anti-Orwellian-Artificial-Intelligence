 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/browser_extension/background.js b/browser_extension/background.js
new file mode 100644
index 0000000000000000000000000000000000000000..b01abbd6abe1bfaad92db3b66eb6adb3a712ee3f
--- /dev/null
+++ b/browser_extension/background.js
@@ -0,0 +1,9 @@
+chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
+  if (message.type === 'AOAI_LOG') {
+    chrome.storage.local.get({ events: [] }, ({ events }) => {
+      events.push({ ...message.payload, ts: new Date().toISOString() });
+      chrome.storage.local.set({ events });
+    });
+  }
+});
+
 
EOF
)
