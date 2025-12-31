import arxiv
import requests
import pandas as pd
from io import StringIO

def safe_arxiv(query):
    try:
        search = arxiv.Search(query=query, max_results=3)
        return list(search.results())
    except Exception:
        return []

def data_alchemist(state):
    # ✅ FIX: ensure questions are strings
    questions = state.get("questions", [])

    # Flatten and extract keywords safely
    keywords = []
    for q in questions:
        if isinstance(q, str):
            keywords.extend(q.replace("?", "").split()[:5])

    keyword_query = " ".join(keywords[:10])  # arXiv-safe length

    papers = safe_arxiv(keyword_query)

    sources = [
        {
            "type": "paper",
            "title": p.title,
            "summary": p.summary,
            "link": p.entry_id
        }
        for p in papers
    ]

    # CSV source + cleaning
    csv_text = requests.get(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv",
        timeout=10
    ).text

    df = pd.read_csv(StringIO(csv_text)).dropna()
    stats = df.describe().to_dict()

    sources.append({
        "type": "csv_cleaned",
        "stats": stats
    })

    # Web/domain signal
    sources.append({
        "type": "web",
        "text": " ".join(state.get("domains", []))
    })

    return {**state, "data_sources": sources}



