import arxiv
import json
from tools.llm import llm
from tools.web_search import simple_web_search
from memory.pinecone_memory import retrieve_memory

def domain_scout(state):
    past = retrieve_memory("emerging scientific domains")

    search = arxiv.Search(
        query="machine learning",
        max_results=20,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    raw_signals = []
    for p in search.results():
        if p.published.year >= 2024:
            raw_signals.append(f"{p.title}. {p.summary[:200]}")

    web_signals = simple_web_search(
        "emerging AI research topics 2024 2025 site:arxiv.org"
    )

    prompt = f"""
    From the following research signals, identify 5 emerging scientific domains
    (post-2024). These must be concise topic names, not arXiv categories.

    Signals:
    {raw_signals + web_signals}

    Respond ONLY in valid JSON like:
    ["Domain 1", "Domain 2", "Domain 3", "Domain 4", "Domain 5"]
    """

    response = llm.invoke(prompt).content.strip()

    try:
        domains = json.loads(response)
    except Exception:
        # safe fallback if model still misbehaves
        domains = [
            "AI-driven Scientific Discovery",
            "Foundation Models for Science",
            "Autonomous Research Agents",
            "AI for Materials Design",
            "Machine Learning Systems"
        ]

    return {
        **state,
        "domains": domains[:5],
        "past_memory": past
    }


