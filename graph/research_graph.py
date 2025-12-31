from langgraph.graph import StateGraph, END
from agents.supervisor import supervisor
from agents.domain_scout import domain_scout
from agents.question_generator import question_generator
from agents.data_alchemist import data_alchemist
from agents.eda import eda
from agents.experiment_designer import experiment_designer
from agents.critic import critic
from agents.uncertainty import uncertainty
from agents.paper_writer import paper_writer

def build_graph():
    g = StateGraph(dict)

    g.add_node("supervisor", supervisor)
    g.add_node("domain", domain_scout)
    g.add_node("question", question_generator)
    g.add_node("data", data_alchemist)
    g.add_node("eda", eda)
    g.add_node("experiment", experiment_designer)
    g.add_node("critic", critic)
    g.add_node("uncertainty", uncertainty)
    g.add_node("paper", paper_writer)

    g.set_entry_point("supervisor")

    g.add_edge("supervisor", "domain")
    g.add_edge("domain", "question")
    g.add_edge("question", "data")
    g.add_edge("data", "eda")
    g.add_edge("eda", "experiment")
    g.add_edge("experiment", "critic")

    #  SINGLE, GUARANTEED EXIT LOGIC
    g.add_conditional_edges(
        "critic",
        lambda s: "end" if s.get("stop") or s["decision"] == "ACCEPT" else "retry",
        {
            "retry": "supervisor",
            "end": "uncertainty"
        }
    )

    g.add_edge("uncertainty", "paper")
    g.add_edge("paper", END)

    return g.compile()

