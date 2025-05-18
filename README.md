# 🛡️ VulnDetector

**VulnDetector** is a lightweight Python tool that scans websites for missing or weak HTTP security headers — a quick way to catch low-hanging web security issues.

---

## ✨ Features

* 🔍 Scans for key HTTP security headers:

  * `Content-Security-Policy`
  * `X-Frame-Options`
  * `Strict-Transport-Security`
  * `X-Content-Type-Options`
  * `Referrer-Policy`
  * `Permissions-Policy`
* 🧠 Simple and beginner-friendly codebase
* 🧪 Clean CLI experience
* ⚠️ Handles connection errors gracefully
* 🐍 Built with Python

---

## 🚀 Installation

1. **Clone the repo**:

   ```bash
   git clone https://github.com/your-username/VulnDetector.git
   cd VulnDetector
   ```

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

Run the script like this:

```bash
python vuln_detector.py
```

Then enter the full URL (including `http://` or `https://`) when prompted:

```
Enter website URL (with http/https): https://example.com
```

---

## 📊 Example Output

```
[+] Security Header Check:

[✔] Content-Security-Policy is present.
[!] X-Frame-Options is missing!
[✔] Strict-Transport-Security is present.
[✔] X-Content-Type-Options is present.
[!] Referrer-Policy is missing!
[✔] Permissions-Policy is present.
```

---

## 🌱 Future Plans

* 🧠 Add BeautifulSoup support to analyze HTML content
* 📁 Export results to a report file
* 🎨 Add color-coded terminal output
* 🔄 Scan multiple URLs in a batch
* 🔐 Expand detection to include cookie flags and SSL info

---

## 🤝 Contributing

Have ideas or improvements? Feel free to fork the repo, open issues, or submit pull requests.

---
