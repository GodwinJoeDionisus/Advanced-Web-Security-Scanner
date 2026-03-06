import requests

def load_payloads():
    payloads = []

    with open("../payloads/xss_payloads.txt", "r") as file:
        for line in file:
            payloads.append(line.strip())

    return payloads


def check_xss(url):

    payloads = load_payloads()

    print("\nStarting XSS scan on:", url)

    for payload in payloads:

        test_url = url + payload

        try:
            response = requests.get(test_url, verify=False)

            if payload in response.text:
                print("\n⚠ XSS vulnerability detected!")
                print("URL:", test_url)
                print("Payload:", payload)
                return

        except:
            pass

    print("No XSS detected.")


if __name__ == "__main__":

    target = input("Enter target URL with parameter (example: http://site.com/page?q=): ")

    check_xss(target)