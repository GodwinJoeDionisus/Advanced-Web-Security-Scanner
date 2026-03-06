# 🛡 Advanced Web Security Scanner

An automated web vulnerability scanner built in Python that identifies common web application security issues including **SQL Injection, Cross-Site Scripting (XSS), missing security headers, and technology disclosure**.

The project demonstrates how professional security tools perform automated vulnerability discovery through **crawling, payload injection, response analysis, and security reporting**.

---

# 📌 Project Overview

Modern web applications are vulnerable to various security issues. Security scanners automate the process of detecting vulnerabilities.

This project implements a **modular web security scanning framework** that performs:

* Web crawling
* Parameter discovery
* Vulnerability scanning
* Security misconfiguration detection
* Technology fingerprinting
* Scan result visualization
* Automated report generation

The scanner architecture is inspired by tools like:

* OWASP ZAP
* Nikto
* Burp Suite

---

# 🚀 Features

✔ Website crawler for endpoint discovery
✔ SQL Injection vulnerability detection
✔ Cross-Site Scripting (XSS) detection
✔ Security header analysis
✔ Web technology detection
✔ Flask dashboard for scan visualization
✔ PDF vulnerability report generation

---

# 🧠 System Architecture

Target Website
↓
Crawler Engine
↓
Vulnerability Scanners

* SQL Injection Scanner
* XSS Scanner
* Security Header Analyzer
* Technology Detection

↓
Dashboard Visualization
↓
Security Report Generation

---

# ⚙ Technologies Used

| Technology    | Purpose                    |
| ------------- | -------------------------- |
| Python        | Core programming language  |
| Requests      | HTTP requests for scanning |
| BeautifulSoup | HTML parsing for crawling  |
| Flask         | Dashboard interface        |
| ReportLab     | PDF report generation      |

---

# 📂 Project Structure

```
Advanced-Web-Security-Scanner
│
├── scanner
│   ├── crawler.py
│   ├── sqli_scanner.py
│   ├── xss_scanner.py
│   ├── headers_check.py
│   └── tech_detection.py
│
├── payloads
│   ├── sqli_payloads.txt
│   └── xss_payloads.txt
│
├── dashboard
│   └── app.py
│
├── reports
│   └── report_generator.py
│
├── README.md
└── .gitignore
```

---

# 🔎 Module Explanation

## 1️⃣ Web Crawler

File:

```
scanner/crawler.py
```

Discovers URLs within the target website by parsing HTML links.

Example output:

```
Scanning: https://example.com
Discovered URL: https://example.com/about
Discovered URL: https://example.com/contact
```

---

## 2️⃣ SQL Injection Scanner

File:

```
scanner/sqli_scanner.py
```

Tests parameters using SQL payloads.

Example payloads:

```
' OR '1'='1
' UNION SELECT NULL--
```

The scanner analyzes responses for database error patterns.

---

## 3️⃣ Cross-Site Scripting Scanner

File:

```
scanner/xss_scanner.py
```

Injects XSS payloads and checks if they are reflected in the response.

Example payload:

```
<script>alert(1)</script>
```

---

## 4️⃣ Security Headers Scanner

File:

```
scanner/headers_check.py
```

Checks for missing security headers:

| Header                    | Purpose               |
| ------------------------- | --------------------- |
| Content-Security-Policy   | Prevents XSS          |
| X-Frame-Options           | Prevents clickjacking |
| Strict-Transport-Security | Enforces HTTPS        |
| X-Content-Type-Options    | Prevents MIME attacks |

---

## 5️⃣ Technology Detection

File:

```
scanner/tech_detection.py
```

Identifies server and backend technologies.

Example:

```
Server: cloudflare
Technology: PHP
Framework: Laravel
```

---

# 📊 Dashboard

File:

```
dashboard/app.py
```

Displays scan results through a web interface.

## Dashboard

![Dashboard](dashboard.png)

Dashboard shows:

* Target scanned
* Detected vulnerabilities
* Security misconfigurations
* Server technology

Run dashboard:

```
cd dashboard
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 📄 Security Report

File:

```
reports/report_generator.py
```

Generates a **PDF vulnerability report** similar to professional security tools.

Example report contents:

* Target information
* Vulnerabilities detected
* Severity level
* Technology detected

Run report generator:

```
cd reports
python report_generator.py
```

---

# ▶ Running the Scanner

Example SQL Injection scan:

```
cd scanner
python sqli_scanner.py
```

Example XSS scan:

```
python xss_scanner.py
```

Example header scan:

```
python headers_check.py
```

Example technology detection:

```
python tech_detection.py
```

---

# 🎯 Learning Outcomes

This project demonstrates skills in:

* Web application security
* Vulnerability scanning
* Security automation
* HTTP protocol analysis
* Security tool development
* Security reporting

---

# ⚠ Disclaimer

This project is intended for **educational and research purposes only**.

Do not scan systems without authorization.

---

# 👨‍💻 Author

Godwin Joe Dionisus
Cybersecurity Enthusiast focused on:

* Network Security
* Threat Detection
* Security Automation
* AI-driven cybersecurity tools
