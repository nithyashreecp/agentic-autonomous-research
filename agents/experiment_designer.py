from tools.llm import llm

def experiment_designer(state):
    prompt = f"""
Design a simple experiment AND provide a simulated outcome table
to validate the hypothesis below.

Exploratory Analysis:
{state['eda']}

Return:
- Refined hypothesis
- Experiment design
- Simulated results (small table)
"""

    return {
        **state,
        "experiment": llm.invoke(prompt).content
    }

