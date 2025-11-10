const consentToggle = document.getElementById('consentToggle');
const eventsList = document.getElementById('events');
const clearButton = document.getElementById('clearLogs');

function renderEvents(events) {
  eventsList.innerHTML = '';
  events.slice(-10).reverse().forEach(event => {
    const li = document.createElement('li');
    li.textContent = `${event.ts}: ${event.action}`;
    eventsList.appendChild(li);
  });
}

chrome.storage.local.get({ events: [] }, ({ events }) => {
  renderEvents(events);
});

chrome.storage.local.get({ consent: false }, ({ consent }) => {
  consentToggle.checked = consent;
});

consentToggle.addEventListener('change', () => {
  const allowed = consentToggle.checked;
  chrome.storage.local.set({ consent: allowed });
  chrome.runtime.sendMessage({ type: 'AOAI_LOG', payload: { action: allowed ? 'consent_granted' : 'consent_revoked' } });
  chrome.tabs.query({}, (tabs) => {
    tabs.forEach((tab) => {
      if (tab.id) {
        chrome.tabs.sendMessage(tab.id, { type: 'AOAI_SET_CONSENT', allowed });
      }
    });
  });
});

clearButton.addEventListener('click', () => {
  chrome.storage.local.set({ events: [] }, () => renderEvents([]));
});
