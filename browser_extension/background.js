chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'AOAI_LOG') {
    chrome.storage.local.get({ events: [] }, ({ events }) => {
      events.push({ ...message.payload, ts: new Date().toISOString() });
      chrome.storage.local.set({ events });
    });
  }
});

