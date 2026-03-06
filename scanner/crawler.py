import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

visited_urls = set()

def crawl(url):
    try:
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")

        print(f"\nScanning: {url}")

        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])

            if full_url not in visited_urls:
                visited_urls.add(full_url)
                print("Discovered URL:", full_url)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    target = input("Enter target URL: ")
    crawl(target)