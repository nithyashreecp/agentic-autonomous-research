# 🧠 Autonomous Agentic Research Assistant

A fully autonomous, multi-agent AI system that discovers emerging scientific domains, formulates research questions, gathers and cleans data, performs exploratory analysis, designs experiments, critiques its own results, iterates, and finally produces a structured **mini research paper** with confidence scoring — all with **zero human intervention after startup**.

---

## 🚀 Live Application

🔗 **Streamlit App**  
https://agentic-autonomous-research-imprcudar7d34ny22ygujh.streamlit.app

---

## 📌 Problem Statement

Modern scientific research requires synthesizing vast, rapidly evolving information across domains. Manual research workflows are slow, brittle, and do not scale.

This project implements a **fully autonomous agentic AI research assistant** that independently:
- Discovers emerging research domains (post-2024)
- Generates novel research questions
- Collects and cleans heterogeneous data
- Designs and critiques experiments
- Iteratively refines results
- Produces a structured mini-research paper with confidence scores

---

## 🧩 System Overview

The system is built using **LangGraph** to orchestrate multiple specialized agents that collaborate, critique each other, maintain memory, and self-terminate safely.

### Core Characteristics
- Multi-agent collaboration (not single-prompt or RAG-only)
- Autonomous planning and execution
- Iterative self-critique with enforced limits
- Vector memory using Pinecone
- Real-time web + arXiv data acquisition
- Zero human input after “Start Research”

---

## 🤖 Agent Architecture

### Implemented Agents

| Agent | Responsibility |
|-----|---------------|
| **Supervisor Agent** | Controls iteration count, enforces hard stop (max 5 cycles) |
| **Domain Scout Agent** | Discovers emerging domains using arXiv (post-2024) + web signals |
| **Question Generator Agent** | Generates novel research questions from discovered domains |
| **Data Alchemist Agent** | Collects ≥3 data sources (arXiv papers, CSV dataset, web signals) and cleans data |
| **EDA Agent** | Performs exploratory analysis to identify patterns and risks |
| **Experiment Designer Agent** | Designs hypothesis, experiment, and simulated results |
| **Critic Agent** | Rejects weak experiments and forces refinement cycles |
| **Uncertainty Agent** | Assigns confidence score (0.6–0.9) |
| **Paper Writer Agent** | Produces final Markdown research paper and stores memory |

---

## 🔁 Agentic Workflow (Execution Loop)

1. Supervisor initializes iteration
2. Domain discovery (arXiv + web)
3. Research question generation
4. Data acquisition & cleaning
5. Exploratory data analysis
6. Experiment design
7. Critic evaluation  
   - Reject → loop back
   - Accept → proceed
8. Uncertainty scoring
9. Final paper generation
10. Memory stored in Pinecone

---

## 🧠 Memory System

- **Vector DB:** Pinecone (free tier)
- **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2`
- Stores:
  - Final papers
  - Confidence scores
  - Iteration counts
- Retrieved during future runs for contextual awareness

---

## 📊 Output Artifacts

- **Mini Research Paper (Markdown)**
- **Confidence Score**
- **Iteration Summary**
- **Interactive Plotly chart (confidence vs iteration)**

All outputs are generated automatically and displayed in the UI.

---

## 🛠️ Tech Stack

### AI & Orchestration
- LangGraph
- Groq (LLaMA-3.1-8B, free tier)
- LangChain Groq integration

### Data & Memory
- arXiv API
- DuckDuckGo web scraping
- Pinecone Vector Database
- Sentence Transformers

### Frontend & Visualization
- Streamlit
- Plotly

### Deployment
- Streamlit Cloud (live)
- Docker (multi-stage, provided)

---

## 📁 Project Structure


agentic-autonomous-research/
│
├── agents/
│   ├── domain_scout.py
│   ├── question_generator.py
│   ├── data_alchemist.py
│   ├── eda.py
│   ├── experiment_designer.py
│   ├── critic.py
│   ├── uncertainty.py
│   ├── paper_writer.py
│   └── supervisor.py
│
├── graph/
│   └── research_graph.py
│
├── memory/
│   └── pinecone_memory.py
│
├── tools/
│   ├── llm.py
│   └── web_search.py
│
├── outputs/
│   └── last_paper.md
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md


⚙️ How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/<your-username>/agentic-autonomous-research.git
cd agentic-autonomous-research

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX=agentic-research-memory

4️⃣ Run Application
streamlit run app.py

🐳 Docker Support (Optional)

A multi-stage Dockerfile is included for containerized deployment.

docker build -t agentic-research .
docker run -p 8501:8501 agentic-research
