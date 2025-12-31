from memory.pinecone_memory import store_memory

def paper_writer(state):
    refinement_note = (
        "The research underwent multiple agent-driven refinement cycles. "
        "The initial hypothesis and experiment design were revised based on "
        "Critic feedback before reaching the final accepted version."
        if state.get("iteration", 1) > 1
        else "Single-pass analysis."
    )

    paper = f"""
# Mini Research Paper

## Emerging Domains
{state['domains']}

## Research Questions
{state['questions']}

## Data Acquisition & Cleaning
{state['data_sources']}

## Exploratory Analysis
{state['eda']}

## Hypothesis & Experiment Design
{state['experiment']}

## Iterative Self-Critique & Refinement
{state['critique']}

## Iteration Summary
Total Iterations Performed: {state['iteration']}
{refinement_note}

## Confidence Score
{state['confidence']}
"""

    store_memory(paper, {"confidence": state["confidence"], "iterations": state["iteration"]})
    return {**state, "paper": paper}


