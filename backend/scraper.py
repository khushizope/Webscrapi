import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        data = []
        for item in soup.find_all('h2'):  # Example: Extracting all <h2> elements
            data.append(item.get_text())
        return data

    def scrape(self):
        html = self.fetch_page()
        if html:
            return self.parse_page(html)
        return []
