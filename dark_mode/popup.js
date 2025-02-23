document.getElementById('toggle-dark-mode').addEventListener('click', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      function: toggleDarkMode
    });
  });
});

function toggleDarkMode() {
  if (!document.body.style.filter) {
    document.body.style.filter = 'invert(1) hue-rotate(180deg)';
  } else {
    document.body.style.filter = '';
  }
}
