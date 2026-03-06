import requests

def load_payloads():
    payloads = []

    with open("../payloads/sqli_payloads.txt", "r") as file:
        for line in file:
            payloads.append(line.strip())

    return payloads


def check_sqli(url):

    payloads = load_payloads()

    sql_errors = [
        "you have an error in your sql syntax",
        "warning: mysql",
        "unclosed quotation mark",
        "quoted string not properly terminated",
        "sql syntax error"
    ]

    print("\nStarting SQL Injection scan on:", url)

    for payload in payloads:

        test_url = url + payload

        try:
            response = requests.get(test_url, verify=False)

            for error in sql_errors:

                if error.lower() in response.text.lower():
                    print("\n⚠ SQL Injection vulnerability detected!")
                    print("URL:", test_url)
                    print("Payload:", payload)
                    return

        except:
            pass

    print("No SQL Injection detected.")


if __name__ == "__main__":

    target = input("Enter target URL with parameter (example: http://site.com/page?id=1): ")

    check_sqli(target)