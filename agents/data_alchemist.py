import arxiv
import requests
import pandas as pd
from tools.llm import llm

def data_alchemist(state):
    questions = state.get("questions", [])
    keyword_query = " ".join(" ".join(questions).split()[:12])

    # --- Source 1: arXiv papers ---
    papers = []
    try:
        search = arxiv.Search(query=keyword_query, max_results=3)
        for p in search.results():
            papers.append({
                "type": "paper",
                "title": p.title,
                "summary": p.summary,
                "link": p.entry_id
            })
    except Exception:
        pass

    # --- Source 2: GitHub repo signals ---
    github_data = []
    try:
        resp = requests.get(
            f"https://api.github.com/search/repositories?q={keyword_query}&sort=stars",
            timeout=10
        ).json()

        for r in resp.get("items", [])[:5]:
            github_data.append({
                "repo": r["full_name"],
                "stars": r["stargazers_count"],
                "forks": r["forks_count"]
            })
    except Exception:
        pass

    github_df = pd.DataFrame(github_data)

    # --- Source 3: Structured numeric summary ---
    structured_stats = github_df.describe().to_dict() if not github_df.empty else {}

    sources = [
        {"type": "papers", "data": papers},
        {"type": "github_metrics", "data": github_data},
        {"type": "stats", "data": structured_stats}
    ]

    return {**state, "data_sources": sources}



