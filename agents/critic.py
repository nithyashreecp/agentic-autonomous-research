from tools.llm import llm

def critic(state):
    iteration = state.get("iteration", 1)

    # 🚨 Force at least one refinement cycle
    if iteration == 1:
        return {
            **state,
            "decision": "REJECT",
            "critique": (
                "Initial iteration lacks sufficient depth and validation. "
                "Refinement required to strengthen hypothesis and experimental rigor."
            )
        }

    prompt = f"""
Critically evaluate the experiment.

Respond strictly in one of the following formats:

Decision: ACCEPT
or
Decision: REJECT

Experiment:
{state['experiment']}
"""

    response = llm.invoke(prompt).content
    decision = "REJECT" if "REJECT" in response else "ACCEPT"

    return {
        **state,
        "decision": decision,
        "critique": response
    }





