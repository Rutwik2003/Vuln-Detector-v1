# 🛡️ VulnDetector

**VulnDetector** is a powerful yet lightweight web application built with Flask that scans websites for missing or weak HTTP security headers — a fast and effective way to uncover basic web security issues. It features a modern, dark-themed UI with actionable recommendations and resolution steps.

---

## ✨ Features

- ✅ **Scans for key HTTP security headers** (with weighted importance)  
- 📈 **Calculates a security score** based on detected headers  
- 🎨 **Modern dark-themed UI** with Tailwind CSS, featuring color-coded results (green = present, red = missing, yellow = scores/recommendations)  
- 🧠 **Actionable recommendations** with a dedicated page for resolution steps  
- 📁 **Responsive and wide layout** for better readability  
- ⚠️ **Graceful handling of connection errors** with user-friendly error messages  
- 🚀 **Deployable on Vercel** for public access  
- 🐍 **Beginner-friendly Python/Flask codebase**

---

## 🔎 Headers Scanned

Weighted headers include (but are not limited to):

- `Strict-Transport-Security` (Weight: 20, High)  
- `Content-Security-Policy` (Weight: 20, High)  
- `X-Content-Type-Options` (Weight: 15, Medium)  
- `X-Frame-Options` (Weight: 15, Medium)  
- `Referrer-Policy` (Weight: 10, Medium)  
- `Permissions-Policy` (Weight: 8, Low)  
- `Cross-Origin-Opener-Policy` (Weight: 6, Low)  
- `Cross-Origin-Resource-Policy` (Weight: 6, Low)  
- `X-XSS-Protection` (Weight: 5, Low, deprecated)  
- `Expect-CT` (Weight: 4, Low, deprecated)  
- `NEL` (Weight: 2, Low)  
- `Report-To` (Weight: 2, Low)  

Additionally, it checks for insecure headers like `X-Powered-By`, `Server-Tokens`, and `X-AspNet-Version`.

Each header contributes a different weight to the final security score.

---

## 🚀 Installation

1. **Clone the repository** (or ensure you have the project files):

   ```bash
   git clone https://github.com/Haruki993/VulnDetector.git
   cd VulnDetector
   ```

2. **Install dependencies**:

   Ensure Python 3.9+ is installed, then install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   Dependencies include `Flask==2.3.2`, `requests==2.31.0`, and `validators==0.20.0`.

---

## 🛠️ Usage

### Running Locally

Run the Flask web application with a single command:

```bash
python api/index.py
```

- The app will start at `http://127.0.0.1:5000`.  
- Open `http://127.0.0.1:5000` in a browser to access the scanner.

### Using the Web App

1. **Scan a URL**:

   - Enter a website URL (e.g., `https://example.com`) in the input field.  
   - Click "Scan Now" to analyze the security headers.  
   - View the results, including:  
     - Security score (e.g., 45.45%) in yellow.  
     - Present headers in green, missing headers in red.  
     - Server information, warnings (red), and recommendations (yellow).  
   - If recommendations are present (e.g., "Add includeSubDomains to HSTS"), a "How to Resolve Issues" button will appear.

2. **Resolve Issues**:

   - Click "How to Resolve Issues" to navigate to a dedicated page (`resolve.html`).  
   - Follow the provided steps to address each recommendation (e.g., adding `includeSubDomains` to HSTS with Apache/Nginx configs).  
   - Click "Back to Scanner" to return to the main page.

### Deploying to Vercel

1. **Install Vercel CLI**:

   ```bash
   npm install -g vercel
   ```

2. **Log in to Vercel**:

   ```bash
   vercel login
   ```

3. **Deploy**:

   ```bash
   vercel
   ```

   For production deployment:

   ```bash
   vercel --prod
   ```

4. **Verify**:

   - Visit the Vercel URL (e.g., `https://vulndetector.vercel.app`) and test the scanner.  
   - Use `securityheaders.com` to verify the site’s own security headers (configured in `vercel.json`).

---

## 📊 Sample Output

After scanning `https://example.com`, the web UI might display:

```
Results for https://example.com (Status: 200)

Security Header Score: 45.45%

Present Headers
- Strict-Transport-Security (Severity: High)
  Value: max-age=31536000
  Enforces HTTPS connections
- X-Content-Type-Options (Severity: Medium)
  Value: nosniff
  Prevents MIME-type sniffing

Missing Headers
- Content-Security-Policy (Severity: High)
  Prevents XSS and data injection
- Referrer-Policy (Severity: Medium)
  Controls referrer information

Server Information: cloudflare

Recommendations
- Add includeSubDomains to HSTS

[How to Resolve Issues]
```

Clicking "How to Resolve Issues" takes you to a page with steps like:

```
Resolution Steps

Add includeSubDomains to HSTS
Your Strict-Transport-Security (HSTS) header does not include the includeSubDomains directive, which means subdomains are not forced to use HTTPS. To fix this:

- Modify your HSTS header to include includeSubDomains.
- Example: Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
- If using Apache, add to your .htaccess or server config:
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
- If using Nginx, add to your server block:
  add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
- Restart your server after making changes.
```

---

## 🌱 Future Plans

- 🔄 **Batch scan multiple URLs** via a web form  
- 🧁 **Enhanced UI features** (e.g., score visualization with charts)  
- 🔐 **Expand detection** to include cookie flags and SSL cert info  
- 📊 **Generate downloadable reports** (e.g., PDF export)  
- 🛠️ **More resolution steps** for additional headers  

---

## 🤝 Contributing

Found a bug? Want to improve it? Feel free to fork, submit PRs, or open issues. Let’s make the web a bit safer — one header at a time.

---

## ⚠️ Disclaimer

This tool is intended for **educational and ethical** use only. Do not scan websites without proper authorization.