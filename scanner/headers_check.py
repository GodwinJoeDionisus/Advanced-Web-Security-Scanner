import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests

def check_headers(url):

    print("\nChecking security headers for:", url)

    try:
        response = requests.get(url, verify=False)
        headers = response.headers

        security_headers = {
            "Content-Security-Policy": "Prevents XSS attacks",
            "X-Frame-Options": "Prevents clickjacking",
            "Strict-Transport-Security": "Enforces HTTPS",
            "X-Content-Type-Options": "Prevents MIME sniffing"
        }

        for header, description in security_headers.items():

            if header in headers:
                print(f"✓ {header} is present")
            else:
                print(f"⚠ Missing {header} ({description})")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":

    target = input("Enter target URL (example: https://example.com): ")

    check_headers(target)