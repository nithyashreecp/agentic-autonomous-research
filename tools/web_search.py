import requests
from bs4 import BeautifulSoup

def simple_web_search(query):
    url = f"https://duckduckgo.com/html/?q={query}"
    html = requests.get(url, timeout=10).text
    soup = BeautifulSoup(html, "html.parser")

    results = []
    for a in soup.select("a.result__a")[:5]:
        results.append(a.text)

    return results
