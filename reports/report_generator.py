from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(target, results):

    filename = "scan_report.pdf"

    pdf = canvas.Canvas(filename, pagesize=letter)

    pdf.setFont("Helvetica", 16)
    pdf.drawString(200, 750, "Web Security Scan Report")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(50, 700, f"Target: {target}")

    y = 650

    pdf.drawString(50, y, "Detected Vulnerabilities")
    y -= 30

    for vuln, status in results.items():

        pdf.drawString(70, y, f"{vuln}: {status}")
        y -= 20

    pdf.save()

    print(f"Report generated: {filename}")


if __name__ == "__main__":

    target = "example.com"

    results = {
        "SQL Injection": "Detected",
        "Cross Site Scripting": "Detected",
        "Missing Security Headers": "Yes",
        "Server": "Cloudflare"
    }

    generate_report(target, results)