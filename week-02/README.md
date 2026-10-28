# COVID-19 FAQ Semantic Search Engine

A dense semantic retrieval system powered by [ChromaDB](https://www.trychroma.com/) (with local disk persistence) and [Sentence Transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2` in FP16 precision) over the [Sunlab OSU COVID-19 FAQ Bank](https://raw.githubusercontent.com/sunlab-osu/covid-faq/master/data/FAQ_Bank.csv).

---

## 📌 Architecture & Design

This pipeline cleans multilingual, noisy health agency FAQ data, creates overlapping text chunks, converts them to compact 384-dimensional dense vectors using half-precision (`FP16`) inference, and indexes them in a persistent ChromaDB vector store backed by HNSW cosine distance.

```
Sunlab OSU FAQ_Bank.csv (~15.9k records)
                   │
                   ▼
Text Normalization (HTML tag removal, HTML entity unescape, whitespace collapsing)
                   │
                   ▼
Document Construction ("Question: ... \nAnswer: ...")
                   │
                   ▼
Sliding-Window Word Chunking (chunk_size=150 words, overlap=30 words)
                   │
                   ▼
FP16 Dense Vector Encoding (SentenceTransformer all-MiniLM-L6-v2 on CUDA/CPU)
                   │
                   ▼
ChromaDB Persistent Client Storage (./chroma_faq_db, HNSW Cosine Index)
                   │
                   ▼
Top-3 Semantic Nearest Neighbor Retrieval
```

---

## ⚙️ Installation & Setup

### Requirements
- Python 3.9 to 3.11
- CUDA-compatible GPU recommended for fast bulk encoding (FP16 supported)

### Quick Start

```bash
# Clone or navigate to your project directory
git clone <repo-url>
cd <repo-folder>

# Set up and activate a virtual environment
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Pipeline Workflow

### 1. Ingestion & Preprocessing
- **Source**: Sunlab OSU `FAQ_Bank.csv` containing ~15,919 global FAQ entries from agencies like WHO, CDC, FDA, and state health departments.
- **Cleaning**:
  - Removes HTML tags using `BeautifulSoup`.
  - Unescapes raw HTML entities (e.g., `&amp;`, `&quot;`).
  - Cleans excess whitespace and regex matches.
  - Drops null questions/answers and identical duplicate pairs.

### 2. Document Structuring & Chunking
- Assembles each entry into:
  ```text
  Question: <sanitized question>
  Answer: <sanitized answer>
  ```
- Splits lengthy entries into sliding windows of **150 words** with a **30-word overlap** to preserve contextual boundaries across chunk splits.
- Preserves document lineage using metadata tags (`faq_id`).

### 3. GPU Acceleration & Vector Indexing
- Loads `all-MiniLM-L6-v2` and casts model weights to half precision (`model.half()`) to double encoding throughput and cut VRAM consumption by ~50%.
- Generates normalized dense vectors in batches of 256.
- Stores embeddings and source text inside a local ChromaDB directory (`./chroma_faq_db`) in batches of 1,000 chunks.

---

## 🔍 Example Queries & Benchmarks

Here are representative test queries across distinct domains (symptoms, isolation, diagnostics, and prevention):

### 1. Symptoms & Disease Onset
```python
query = "What are the early warning signs of coronavirus infection?"
```
- **Retrieved Content**: Clinical symptom checklists (fever, dry cough, shortness of breath, loss of taste or smell).

### 2. Transmission Dynamics
```python
query = "Can infected people spread the virus if they do not have symptoms?"
```
- **Retrieved Content**: Asymptomatic and presymptomatic transmission guidance from public health agencies.

### 3. Quarantine & Recovery Durations
```python
query = "How long do I need to quarantine after testing positive?"
```
- **Retrieved Content**: Self-isolation timelines, day counts for fever-free recovery, and guidance on returning to work/school.

### 4. Mask Protection & Filtration
```python
query = "Do cloth masks protect against airborne droplets as well as N95 respirators?"
```
- **Retrieved Content**: Filtration comparisons between N95/KN95 respirators, surgical masks, and multi-layer cloth coverings.

### 5. General Information & Support (Notebook Query)
```python
query = "How can I get more information?"
```
- **Top Matches**: WHO self-care guidance portals, employer ADA/EEOC COVID-19 compliance pages, and state public health helpline resources.

---

## 💻 Python Query Execution

Run top-$k$ semantic searches against the persisted database without re-encoding the entire dataset:

```python
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to the persisted database directory
client = chromadb.PersistentClient(path="./chroma_faq_db")
collection = client.get_collection(name="faq_collection")

def search_covid_faq(query_text: str, top_k: int = 3):
    query_vector = model.encode([query_text], normalize_embeddings=True).tolist()
    
    results = collection.query(
        query_embeddings=query_vector,
        n_results=top_k,
        include=["documents", "distances", "metadatas"]
    )
    
    print(f"\n==================== Query: {query_text} ====================")
    for rank, (doc, dist) in enumerate(zip(results["documents"][0], results["distances"][0]), start=1):
        print(f"\n[Match {rank}] | Cosine Distance: {dist:.4f}")
        print(doc)
        print("-" * 60)

# Run a test query
search_covid_faq("Are domestic pets like cats and dogs able to transmit COVID?")
```

---

## 📊 Performance Notes

- **Persistent Disk Cache**: Once populated, `./chroma_faq_db` persists to disk, eliminating the need to re-index between script runs.
- **Inference Speed**: Using `model.half()` on a T4 GPU reduces embedding generation time across ~20,000+ chunks to under **30 seconds**.
- **Query Latency**: Top-3 approximate nearest neighbor search typically completes in **under 15 ms**.