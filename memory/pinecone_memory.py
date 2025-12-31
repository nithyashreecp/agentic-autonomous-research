import os
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import uuid

load_dotenv()

INDEX_NAME = os.getenv("PINECONE_INDEX", "agentic-research-memory")

embedder = SentenceTransformer("all-MiniLM-L6-v2")

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# ❌ DO NOT CREATE INDEX AUTOMATICALLY
# ✔ Assume index already exists (free-tier safe)
index = pc.Index(INDEX_NAME)


def store_memory(text, metadata=None):
    if metadata is None:
        metadata = {}

    vector = embedder.encode(text).tolist()
    index.upsert([{
        "id": str(uuid.uuid4()),
        "values": vector,
        "metadata": metadata
    }])


def retrieve_memory(query, top_k=3):
    vector = embedder.encode(query).tolist()
    res = index.query(
        vector=vector,
        top_k=top_k,
        include_metadata=True
    )

    return [m["metadata"] for m in res.get("matches", [])]
