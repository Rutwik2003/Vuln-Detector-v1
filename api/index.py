import requests
import json
import os
from flask import Flask, request, jsonify, render_template
from urllib.parse import urlparse
import validators

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__,
            template_folder=os.path.join(base_dir, "../public"),
            static_folder=os.path.join(base_dir, "../public"),
            static_url_path="")

# Security headers configuration
security_headers = {
    "Strict-Transport-Security": {"weight": 20, "severity": "High", "description": "Enforces HTTPS connections"},
    "Content-Security-Policy": {"weight": 20, "severity": "High", "description": "Prevents XSS and data injection"},
    "X-Content-Type-Options": {"weight": 15, "severity": "Medium", "description": "Prevents MIME-type sniffing"},
    "X-Frame-Options": {"weight": 15, "severity": "Medium", "description": "Prevents clickjacking"},
    "Referrer-Policy": {"weight": 10, "severity": "Medium", "description": "Controls referrer information"},
    "Permissions-Policy": {"weight": 8, "severity": "Low", "description": "Controls feature permissions"},
    "Cross-Origin-Opener-Policy": {"weight": 6, "severity": "Low", "description": "Controls cross-origin access"},
    "Cross-Origin-Resource-Policy": {"weight": 6, "severity": "Low", "description": "Controls resource sharing"},
    "X-XSS-Protection": {"weight": 5, "severity": "Low", "description": "Legacy XSS protection (deprecated)"},
    "Expect-CT": {"weight": 4, "severity": "Low", "description": "Enforces Certificate Transparency (deprecated)"},
    "NEL": {"weight": 2, "severity": "Low", "description": "Network Error Logging"},
    "Report-To": {"weight": 2, "severity": "Low", "description": "Reporting endpoint configuration"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_headers():
    url = request.json.get('url')
    if not url or not validators.url(url):
        return jsonify({"error": "Invalid or missing URL"}), 400

    try:
        headers = {'User-Agent': 'Security-Header-Scanner/2.0'}
        response = requests.get(url, timeout=10, headers=headers, allow_redirects=True)
        response_headers = response.headers
        status_code = response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to connect: {str(e)}"}), 500

    domain = urlparse(url).netloc
    total_weight = sum(header["weight"] for header in security_headers.values())
    response_keys = {k.lower() for k in response_headers.keys()}
    score = 0
    results = {"domain": domain, "url": url, "status_code": status_code, "headers": {}, "missing_headers": [], "score": 0, "insecure_headers": [], "warnings": [], "recommendations": []}

    for header, info in security_headers.items():
        if header.lower() in response_keys:
            results["headers"][header] = {"status": "Present", "value": response_headers.get(header, ""), "description": info["description"], "severity": info["severity"]}
            score += info["weight"]
        else:
            results["missing_headers"].append({"header": header, "severity": info["severity"], "description": info["description"]})

    score_percent = (score / total_weight) * 100
    results["score"] = round(score_percent, 2)

    if 'Server' in response_headers:
        results["server_info"] = response_headers['Server']

    insecure_headers = ['X-Powered-By', 'Server-Tokens', 'X-AspNet-Version']
    for header in insecure_headers:
        if header in response_headers:
            results["insecure_headers"].append({header: response_headers[header]})

    if 'Strict-Transport-Security' in response_headers:
        hsts = response_headers['Strict-Transport-Security']
        if 'max-age=0' in hsts:
            results["warnings"].append("HSTS max-age set to 0")
        elif 'includeSubDomains' not in hsts:
            results["recommendations"].append("Add includeSubDomains to HSTS")

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)