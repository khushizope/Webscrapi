document.getElementById('scrapeBtn').addEventListener('click', async () => {
    const url = document.getElementById('urlInput').value;
    const response = await fetch('/scrape', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
    });
    const data = await response.json();
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '<ul>' + data.map(item => `<li>${item}</li>`).join('') + '</ul>';
});
