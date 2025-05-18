# 🛡️ VulnDetector

**VulnDetector** is a powerful yet lightweight Python tool that scans websites for missing or weak HTTP security headers — a fast and effective way to uncover basic web security issues.

---

## ✨ Features

- ✅ **Scans for key HTTP security headers** (with weighted importance)  
- 📈 **Calculates a security score** based on detected headers  
- 🎨 **Color-coded terminal output** (green = good, red = missing, yellow = scores)  
- 🧠 **Heuristic detection** of custom or suspicious headers  
- 📁 **Optional export to a result file**  
- ⚠️ **Graceful handling of connection errors**  
- 🐍 **Beginner-friendly Python codebase**

---

## 🔎 Headers Scanned

Weighted headers include (but are not limited to):

- `Strict-Transport-Security`
- `Content-Security-Policy`
- `X-Content-Type-Options`
- `X-Frame-Options`
- `Referrer-Policy`
- `Permissions-Policy`
- `Access-Control-Allow-Origin`
- `Expect-CT`
- `Cross-Origin-Opener-Policy`
- `Cross-Origin-Resource-Policy`
- `X-XSS-Protection`
- `Cache-Control`
- `NEL`
- `Report-To`
- `Feature-Policy`
- `X-Permitted-Cross-Domain-Policies`

Each header contributes a different weight to the final score.

---

## 🚀 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Haruki993/VulnDetector.git
   cd VulnDetector
````

2. **(Optional)** Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

Run the script:

```bash
python vuln_detector.py
```

Then enter the website URL (with `http://` or `https://`) when prompted:

```
Enter website URL (with http/https): https://example.com
```

You’ll be asked if you want to export the results to a file.

---

## 📊 Sample Output

```
[✔] Strict-Transport-Security (Weight: 20): Present
[✔] Content-Security-Policy (Weight: 20): Present
[✖] Referrer-Policy (Weight: 10): Missing

[+] Overall Security Header Score: 80.00%

[+] Heuristic Header Detection:
[?] Possibly interesting: X-Example-Custom-Security -> Value123
```

---

## 🌱 Future Plans

* 🔄 Batch scan multiple URLs
* 🧁 GUI support (Tkinter or CLI menu)
* 🔐 Expand detection to include cookie flags and SSL cert info
* 📊 Generate HTML reports

---

## 🤝 Contributing

Found a bug? Want to improve it?
Feel free to fork, submit PRs, or open issues.
Let's make the web a bit safer — one header at a time.

---

## ⚠️ Disclaimer

This tool is intended for **educational and ethical** use only.
Do not scan websites without proper authorization.

````
