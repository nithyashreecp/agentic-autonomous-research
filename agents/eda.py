from tools.llm import llm

def eda(state):
    prompt = f"""
Perform exploratory analysis on the following cleaned data summary.
Identify patterns and risks.

{state['data_sources']}
"""
    return {**state, "eda": llm.invoke(prompt).content}
