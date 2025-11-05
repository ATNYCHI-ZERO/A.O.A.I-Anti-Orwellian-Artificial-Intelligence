diff --git a/browser_extension/popup.js b/browser_extension/popup.js
new file mode 100644
index 0000000000000000000000000000000000000000..92f0459ebfa967f798e9f6854912b0cbe306e147
--- /dev/null
+++ b/browser_extension/popup.js
@@ -0,0 +1,37 @@
+const consentToggle = document.getElementById('consentToggle');
+const eventsList = document.getElementById('events');
+const clearButton = document.getElementById('clearLogs');
+
+function renderEvents(events) {
+  eventsList.innerHTML = '';
+  events.slice(-10).reverse().forEach(event => {
+    const li = document.createElement('li');
+    li.textContent = `${event.ts}: ${event.action}`;
+    eventsList.appendChild(li);
+  });
+}
+
+chrome.storage.local.get({ events: [] }, ({ events }) => {
+  renderEvents(events);
+});
+
+chrome.storage.local.get({ consent: false }, ({ consent }) => {
+  consentToggle.checked = consent;
+});
+
+consentToggle.addEventListener('change', () => {
+  const allowed = consentToggle.checked;
+  chrome.storage.local.set({ consent: allowed });
+  chrome.runtime.sendMessage({ type: 'AOAI_LOG', payload: { action: allowed ? 'consent_granted' : 'consent_revoked' } });
+  chrome.tabs.query({}, (tabs) => {
+    tabs.forEach((tab) => {
+      if (tab.id) {
+        chrome.tabs.sendMessage(tab.id, { type: 'AOAI_SET_CONSENT', allowed });
+      }
+    });
+  });
+});
+
+clearButton.addEventListener('click', () => {
+  chrome.storage.local.set({ events: [] }, () => renderEvents([]));
+});
