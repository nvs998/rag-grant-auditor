# 🎬 Lunim Film Suite — RAG Grant & Investor Readiness Auditor

An end-to-end Retrieval-Augmented Generation (RAG) diagnostic engine designed to help independent filmmakers evaluate draft pitch treatments against regional grant mandates, financial compliance rules, legal chain-of-title parameters, and technical deliverable standards before formal submission.

---

## 📌 Features

- **Automated Compliance Auditing:** Evaluates film pitch treatments against retrieved compliance mandates across four core operational pillars.
- **RAG-Driven Grounding:** Queries a local ChromaDB vector store to ground LLM audit reports directly in official guideline clauses (e.g. `[SECTION 2.1]`).
- **Categorized Diagnostic Output:** Generates structured report cards detailing overall readiness scores, category-by-category breakdowns (`Compliant` / `Partial` / `Non-Compliant`), and actionable next steps.
- **Multi-Pitch Demo Testing:** Toggle between compliant and non-compliant sample pitches.
- **Graceful Error Handling & Fallbacks:** Supports cached responses and offline LLMs (Ollama).

---

## 📐 System Architecture

```text
+-------------------------+
| grant_guidelines.txt    |
+------------+------------+
             |
      (Chunking)
             |
             v
+-------------------------+
| HuggingFace Embeddings  |
+------------+------------+
             |
             v
+-------------------------+
| ChromaDB Vector Store   |
+------------+------------+
             |
             | Similarity Search (k=4)
             v
+-------------------------+
| Retrieved Context       |
+------------+------------+
             ^
             |
+------------+------------+
| Filmmaker Pitch Input   |
+------------+------------+
             |
             v
+-------------------------+
| LangChain Prompt Engine |
+------------+------------+
             |
             v
+-------------------------+
| LLM Inference Engine    |
| HF / Groq / Ollama      |
+------------+------------+
             |
             v
+-------------------------+
| Streamlit UI Dashboard  |
+-------------------------+
```

---

## 🗂️ Project Structure

```text
rag-grant-auditor/
│
├── grant_guidelines.txt
├── sample_pitch_weak.txt
├── sample_pitch_strong.txt
├── ingest.py
├── analyzer.py
├── prompts.py
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## 📋 Compliance Pillars Evaluated

1. **Team Eligibility & Legal Chain of Title (`[SECTION 1]`)**
2. **Financial Mechanics & Revenue Recapture (`[SECTION 2]`)**
3. **Script Feasibility & Technical Deliverables (`[SECTION 3]`)**
4. **Diversity & Sustainability Mandates (`[SECTION 4]`)**

---

## 🚀 Quickstart Guide

### 1. Prerequisites

- Python 3.10+

### 2. Environment Setup

```bash
git clone https://github.com/your-username/rag-grant-auditor.git
cd rag-grant-auditor

# Create virtual environment
python3 -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root folder and add your credentials:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

---

## ⚙️ Running the Pipeline

### Step 1: Ingest Guidelines into Vector DB

Embed and store `grant_guidelines.txt` into ChromaDB:

```bash
python ingest.py
```

### Step 2: Test Analysis via Terminal

Run the diagnostic engine directly against `sample_pitch.txt`:

```bash
python analyzer.py
```

### Step 3: Launch Streamlit Dashboard

Run the interactive web application:

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

in your browser to interact with the interface.
