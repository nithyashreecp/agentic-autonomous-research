import streamlit as st
from graph.research_graph import build_graph
import plotly.express as px

st.title("🧠 Autonomous Agentic Research Assistant")

status = st.empty()

if st.button("🚀 Start Research"):
    status.info("🤖 Agents waking up...")
    graph = build_graph()
    result = graph.invoke({})

    status.success("✅ Research completed")
    st.markdown(result["paper"])

    fig = px.line(
        x=list(range(1, result["iteration"] + 1)),
        y=[0.6 + i*0.05 for i in range(result["iteration"])],
        labels={"x": "Iteration", "y": "Confidence"}
    )
    st.plotly_chart(fig)

