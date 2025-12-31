# ---------- Stage 1: Base ----------
FROM python:3.10-slim AS base

WORKDIR /app

# Install system dependencies (lightweight)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---------- Stage 2: Dependencies ----------
FROM base AS deps

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Stage 3: Runtime ----------
FROM base

COPY --from=deps /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=deps /usr/local/bin /usr/local/bin

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

