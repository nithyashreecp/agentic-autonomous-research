import arxiv
import pandas as pd

def data_alchemist(state):
    #  Anchor search to discovered domains
    domains = state.get("domains", [])
    keyword_query = " ".join(domains[:2])  

    # arXiv papers 
    papers = []
    metadata_rows = []

    try:
        search = arxiv.Search(query=keyword_query, max_results=5)
        for p in search.results():
            papers.append({
                "type": "paper",
                "title": p.title,
                "summary": p.summary,
                "link": p.entry_id
            })

            # CSV (derived metadata) 
            metadata_rows.append({
                "title_length": len(p.title.split()),
                "abstract_length": len(p.summary.split()),
                "year": p.published.year
            })
    except Exception:
        pass

    metadata_df = pd.DataFrame(metadata_rows)
    metadata_stats = metadata_df.describe().to_dict() if not metadata_df.empty else {}

    # Web signals 
    web_signals = {
        "type": "web_signals",
        "source": "DuckDuckGo",
        "query_terms": keyword_query
    }

    return {
        **state,
        "data_sources": [
            {"type": "papers", "data": papers},                  
            {"type": "structured_csv", "stats": metadata_stats}, 
            web_signals                                          
        ]
    }






