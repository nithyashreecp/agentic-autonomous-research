from collections import Counter
import re
from tools.llm import llm

def experiment_designer(state):
    """
    Paper-only, executed experiment:
    - Extract keywords from paper summaries
    - Quantify method trends
    - Produce real numeric results
    """

    papers = []
    for src in state.get("data_sources", []):
        if src.get("type") == "papers":
            papers.extend(src.get("data", []))

    # ---- Extract text ----
    text = " ".join(p.get("summary", "") for p in papers).lower()

    # ---- Simple keyword-based experiment ----
    keywords = [
        "learning", "optimization", "control",
        "robot", "humanoid", "framework",
        "neural", "policy", "interaction"
    ]

    counts = Counter()
    for k in keywords:
        counts[k] = len(re.findall(rf"\b{k}\b", text))

    # ---- Prepare results table ----
    result_table = "\n".join(
        f"{k}: {v}" for k, v in counts.items()
    )

    # ---- LLM interpretation ----
    prompt = f"""
    Based on the following executed experiment results from humanoid robotics papers:

    Keyword Frequency Results:
    {result_table}

    Do the following:
    1. State a refined hypothesis
    2. Describe the experiment design (already executed)
    3. Interpret the results quantitatively
    4. Mention one limitation

    Keep it concise and scientific.
    """

    experiment_report = llm.invoke(prompt).content

    return {
        **state,
        "experiment": experiment_report
    }
