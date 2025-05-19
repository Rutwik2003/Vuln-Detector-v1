async function scanUrl() {
    const urlInput = document.getElementById('urlInput');
    const resultsDiv = document.getElementById('results');
    const errorDiv = document.getElementById('error');
    const loadingDiv = document.getElementById('loading');
    const url = urlInput.value.trim();

    // Reset UI
    resultsDiv.innerHTML = '';
    errorDiv.innerHTML = '';
    errorDiv.classList.add('hidden');
    loadingDiv.classList.remove('hidden');

    // Basic client-side validation
    if (!url) {
        errorDiv.innerHTML = 'Please enter a URL';
        errorDiv.classList.remove('hidden');
        loadingDiv.classList.add('hidden');
        return;
    }

    try {
        const response = await fetch('/scan', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });
        const data = await response.json();

        loadingDiv.classList.add('hidden');

        if (response.ok) {
            let html = `<h3 class="text-xl font-semibold text-gray-100">Results for ${data.url} (Status: ${data.status_code})</h3>`;
            html += `<p class="yellow text-lg font-medium">Security Header Score: ${data.score}%</p>`;
            html += '<h4>Present Headers</h4><ul>';
            for (const [header, info] of Object.entries(data.headers)) {
                html += `<li class="green">${header} (Severity: ${info.severity})<br><span class="text-gray-300">Value: ${info.value}</span><br><span class="text-gray-400 text-sm">${info.description}</span></li>`;
            }
            html += '</ul>';
            if (data.missing_headers.length) {
                html += '<h4>Missing Headers</h4><ul>';
                for (const header of data.missing_headers) {
                    html += `<li class="red">${header.header} (Severity: ${header.severity})<br><span class="text-gray-400 text-sm">${header.description}</span></li>`;
                }
                html += '</ul>';
            }
            if (data.server_info) {
                html += `<p class="text-gray-300">Server Information: ${data.server_info}</p>`;
            }
            if (data.insecure_headers.length) {
                html += '<h4>Insecure Headers</h4><ul>';
                for (const header of data.insecure_headers) {
                    html += `<li class="red">${Object.keys(header)[0]}: ${Object.values(header)[0]}</li>`;
                }
                html += '</ul>';
            }
            if (data.warnings.length) {
                html += '<h4>Warnings</h4><ul>';
                for (const warning of data.warnings) {
                    html += `<li class="red">${warning}</li>`;
                }
                html += '</ul>';
            }
            if (data.recommendations.length) {
                html += '<h4>Recommendations</h4><ul>';
                for (const rec of data.recommendations) {
                    html += `<li class="yellow">${rec}</li>`;
                }
                html += '</ul>';
                // Add button to redirect to resolve.html
                const queryParams = new URLSearchParams();
                queryParams.append('recommendations', JSON.stringify(data.recommendations));
                html += `<a href="resolve.html?${queryParams.toString()}" class="resolve-btn">How to Resolve Issues</a>`;
            }
            resultsDiv.innerHTML = html;
        } else {
            errorDiv.innerHTML = `Error: ${data.error}`;
            errorDiv.classList.remove('hidden');
        }
    } catch (error) {
        loadingDiv.classList.add('hidden');
        errorDiv.innerHTML = `Error: ${error.message}`;
        errorDiv.classList.remove('hidden');
    }
}