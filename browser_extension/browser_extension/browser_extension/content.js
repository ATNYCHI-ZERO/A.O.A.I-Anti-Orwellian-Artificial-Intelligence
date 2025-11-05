 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/browser_extension/content.js b/browser_extension/content.js
new file mode 100644
index 0000000000000000000000000000000000000000..e6cf01c2a4abfe50e06708b5efb5ed4cfa7cee58
--- /dev/null
+++ b/browser_extension/content.js
@@ -0,0 +1,43 @@
+(function () {
+  const CONSENT_KEY = 'aoai_allow_media';
+
+  function hasConsent() {
+    try {
+      return localStorage.getItem(CONSENT_KEY) === 'true';
+    } catch (err) {
+      return false;
+    }
+  }
+
+  const originalGetUserMedia = navigator.mediaDevices && navigator.mediaDevices.getUserMedia;
+  if (!originalGetUserMedia) {
+    return;
+  }
+
+  navigator.mediaDevices.getUserMedia = function (constraints) {
+    if (!hasConsent()) {
+      console.warn('AOAI: blocked getUserMedia (consent required)');
+      window.postMessage({
+        type: 'AOAI_BLOCK',
+        payload: { constraints }
+      }, '*');
+      chrome.runtime.sendMessage({ type: 'AOAI_LOG', payload: { action: 'blocked_getUserMedia', constraints } });
+      return Promise.reject(new Error('AOAI: media access blocked (consent required)'));
+    }
+    return originalGetUserMedia.call(this, constraints);
+  };
+
+  navigator.mediaDevices.addEventListener('devicechange', () => {
+    chrome.runtime.sendMessage({ type: 'AOAI_LOG', payload: { action: 'devicechange' } });
+  });
+
+  chrome.runtime.onMessage.addListener((message) => {
+    if (message.type === 'AOAI_SET_CONSENT') {
+      try {
+        localStorage.setItem(CONSENT_KEY, message.allowed ? 'true' : 'false');
+      } catch (err) {
+        console.warn('AOAI: unable to persist consent flag', err);
+      }
+    }
+  });
+})();
 
EOF
)
