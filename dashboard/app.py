from flask import Flask, render_template_string

app = Flask(__name__)

scan_results = {
    "target": "example.com",
    "sql_injection": "Detected",
    "xss": "Detected",
    "headers": "Missing Security Headers",
    "server": "Cloudflare"
}

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Web Security Scanner Dashboard</title>
</head>

<body>

<h1>🛡 Advanced Web Security Scanner</h1>

<h2>Target: {{target}}</h2>

<h3>Scan Results</h3>

<table border="1">
<tr>
<th>Vulnerability</th>
<th>Status</th>
</tr>

<tr>
<td>SQL Injection</td>
<td>{{sql}}</td>
</tr>

<tr>
<td>XSS</td>
<td>{{xss}}</td>
</tr>

<tr>
<td>Security Headers</td>
<td>{{headers}}</td>
</tr>

<tr>
<td>Server</td>
<td>{{server}}</td>
</tr>

</table>

</body>
</html>
"""

@app.route("/")
def dashboard():

    return render_template_string(
        HTML,
        target=scan_results["target"],
        sql=scan_results["sql_injection"],
        xss=scan_results["xss"],
        headers=scan_results["headers"],
        server=scan_results["server"]
    )


if __name__ == "__main__":
    app.run(debug=True)