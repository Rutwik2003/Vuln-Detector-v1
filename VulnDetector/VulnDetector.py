import requests

# ANSI color codes for colored output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
    except requests.exceptions.RequestException as e:
        print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")
        return

    print("\n[+] All Response Headers:\n")
    for key, value in headers.items():
        print(f"{key}: {value}")

    # Weighted security headers: header -> weight
    security_headers = {
        "Strict-Transport-Security": 20,
        "Content-Security-Policy": 20,
        "X-Content-Type-Options": 15,
        "X-Frame-Options": 15,
        "Referrer-Policy": 10,
        "Permissions-Policy": 8,
        "Cross-Origin-Opener-Policy": 6,
        "Cross-Origin-Resource-Policy": 6,
        "X-XSS-Protection": 5,
        "Expect-CT": 4,
        "NEL": 2,
        "Report-To": 2,
        "Access-Control-Allow-Origin": 3,
        "Cache-Control": 3,
        "Feature-Policy": 1,
        "X-Permitted-Cross-Domain-Policies": 1,
    }

    total_weight = sum(security_headers.values())
    response_keys = {k.lower() for k in headers.keys()}

    print("\n[+] Security Header Check:\n")
    score = 0
    for header, weight in security_headers.items():
        if header.lower() in response_keys:
            print(f"{Colors.GREEN}[✔] {header} (Weight: {weight}): Present{Colors.RESET}")
            score += weight
        else:
            print(f"{Colors.RED}[✖] {header} (Weight: {weight}): Missing{Colors.RESET}")

    # Calculate and show final weighted score
    score_percent = (score / total_weight) * 100
    print(f"\n[+] Overall Security Header Score: {Colors.YELLOW}{score_percent:.2f}%{Colors.RESET}")

    # Heuristic check for suspicious/custom headers
    print("\n[+] Heuristic Header Detection (Suspicious/Custom Security Headers):\n")
    suspicious_keywords = ["policy", "security", "permission", "x-", "access", "cors", "referrer", "cache", "control"]
    flagged = set()
    lower_known = {h.lower() for h in security_headers}

    for key in headers:
        klower = key.lower()
        if any(kw in klower for kw in suspicious_keywords) and klower not in lower_known:
            print(f"[?] Possibly interesting: {key} -> {headers[key]}")
            flagged.add(key)
    if not flagged:
        print("[-] No additional suspicious headers detected.")

    # Ask user if they want to export results to a file
    export = input("\nDo you want to export the results to a file? (y/n): ").strip().lower()
    if export == 'y':
        filename = input("Enter filename (e.g., results.txt): ").strip()
        with open(filename, "w", encoding="utf-8") as f:
            f.write("[+] All Response Headers:\n")
            for key, value in headers.items():
                f.write(f"{key}: {value}\n")

            f.write("\n[+] Security Header Check:\n")
            for header, weight in security_headers.items():
                status = "Present" if header.lower() in response_keys else "Missing"
                f.write(f"{header} (Weight: {weight}): {status}\n")

            f.write(f"\n[+] Overall Security Header Score: {score_percent:.2f}%\n")

            f.write("\n[+] Heuristic Header Detection (Suspicious/Custom Security Headers):\n")
            if flagged:
                for key in flagged:
                    f.write(f"Possibly interesting: {key} -> {headers[key]}\n")
            else:
                f.write("No additional suspicious headers detected.\n")

        print(f"{Colors.GREEN}Results exported successfully to {filename}{Colors.RESET}")

if __name__ == "__main__":
    url = input("Enter website URL (with http/https): ")
    check_security_headers(url)
