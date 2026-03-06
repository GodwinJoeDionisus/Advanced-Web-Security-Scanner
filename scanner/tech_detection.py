import requests

def detect_technology(url):

    print("\nDetecting technologies used by:", url)

    try:
        response = requests.get(url, verify=False)

        headers = response.headers
        html = response.text.lower()

        if "server" in headers:
            print("Server:", headers["Server"])

        if "x-powered-by" in headers:
            print("Technology:", headers["X-Powered-By"])

        if "wordpress" in html:
            print("CMS detected: WordPress")

        if "django" in html:
            print("Framework detected: Django")

        if "laravel" in html:
            print("Framework detected: Laravel")

        if "php" in headers.get("X-Powered-By", "").lower():
            print("Backend Language: PHP")

        print("Technology detection complete.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":

    target = input("Enter target URL: ")

    detect_technology(target)