import arxiv
from tools.web_search import simple_web_search
from memory.pinecone_memory import retrieve_memory

def domain_scout(state):
    past = retrieve_memory("emerging scientific domains")

    search = arxiv.Search(
        query="machine learning",
        max_results=15,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    domains = set()
    for p in search.results():
        if p.published.year >= 2024:
            domains.add(p.primary_category)

    domains.update(simple_web_search("emerging AI research 2024"))
    return {**state, "domains": list(domains)[:5], "past_memory": past}


