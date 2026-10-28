# AWS Student Builder Group — AI/ML Track

**Hands-on AI/ML learning, weekly implementations, and practical experiments.**

This repository documents my progress through the AWS Student Builder Group AI/ML track. It contains weekly programming tasks, Python implementations, Jupyter notebooks, data-processing workflows, and practical experiments in machine learning and AI engineering.

My focus is on understanding concepts through implementation, writing modular and testable code, and building a strong foundation for developing real-world AI/ML applications.


## Repository Structure

```text
aws-sbg-tasks/
├── week-01/
│   ├── requirements.txt
│   ├── data_cleaning.py
│   ├── data_cleaning.ipynb
│   ├── messy_sales.csv
│   └── cleaned_sales.csv
|
├── week-02/
│   ├── README.md
│   ├── requirements.txt
│   ├── semantic_search.py
│   ├── semantic_search.ipynb
│   └── tests/
│       └── test_covid_faq.py
|
├── .gitignore
├── requirements.txt
└── README.md
```

*The structure reflects the current repository organization; future weekly projects may introduce additional modules and directories.*

## Weekly Projects

### Week 01 — Python Data Processing

A small data-processing application focused on transforming raw sales data into a clean, structured dataset.

**What I practiced:**
- Loading and inspecting CSV files with Pandas.
- Identifying and handling missing or inconsistent data.
- Cleaning and transforming tabular data.
- Using NumPy for numerical operations.
- Separating processing logic into reusable Python modules.
- Writing unit tests to validate expected behavior.

**Main files:** `data_cleaning.py`, and `data_cleaning.ipynb`.

[View Week 01 source code](./week-01/data_cleaning.py)

[![Open Week 01 in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mussie56/aws-sbg-tasks/blob/main/week-01/data-cleaning.ipynb)

### Week 02 — FAQ Semantic Search

A mini semantic-search system that retrieves relevant FAQ entries from natural-language queries using text embeddings and ChromaDB.

**What I practiced:**
- Cleaning FAQ questions and answers.
- Normalizing text and removing duplicate records.
- Combining questions and answers into searchable documents.
- Splitting longer documents into overlapping chunks.
- Generating vector embeddings.
- Storing documents and vectors in ChromaDB.
- Retrieving and ranking the top three matches for a query.

**Main files:** `Semantic_Search.py`, and `Semantic_Search.ipynb`.

[View Week 02 source code](./week-02/semantic_search.py)

[![Open Week 02 in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mussie56/aws-sbg-tasks/blob/main/week-02/Semantic_Search.ipynb)

### Upcoming Projects

Future tasks will be added as the program progresses. Each project will have its own documentation, implementation, relevant data, and reproducible examples.

## Getting Started

You can explore the projects directly in Google Colab or run them locally.

### Prerequisites

- Python 3.10 or newer.
- Git.
- A virtual environment for local development.
- Jupyter Notebook for interactive execution.

### 1. Clone the repository

```bash
git clone https://github.com/mussie56/aws-sbg-tasks.git
cd aws-sbg-tasks
```

### 2. Create a virtual environment

**Windows — PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux or macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Some weekly projects may require additional dependencies. Check the corresponding week's `README.md` and `requirements.txt` before running it.

### 4. Run a project

Run Week 01:

```bash
python week-01/data_cleaning.py
```

Run Week 02:

```bash
python week-02/Semantic_Search.py
```

### 6. Open a notebook

```bash
jupyter notebook week-01/data_cleaning.ipynb
```

To explore semantic search interactively:

```bash
jupyter notebook week-02/Semantic_Search.ipynb
```

## Development Practices

Each project aims to follow these practices:

- **Modularity:** keep core logic separate from application entry points.
- **Reproducibility:** document dependencies, data sources, and execution steps.
- **Testing:** validate important functions with automated tests.
- **Data quality:** inspect inputs and verify outputs before using them downstream.
- **Version control:** use meaningful commits that communicate the changes made.
- **Documentation:** include project objectives, implementation details, and usage examples.
- **Responsible data handling:** respect dataset licenses and avoid committing sensitive information or credentials.


## Learning Objectives

Through these weekly implementations, I aim to strengthen my ability to:

1. Build reliable Python data-processing pipelines.
2. Transform raw data into useful representations.
3. Understand embeddings and vector-based information retrieval.
4. Design modular, testable AI/ML components.
5. Evaluate implementation choices and debug practical problems.
6. Develop reproducible workflows that can serve as building blocks for larger AI applications.


## Author

**Mussie Ferede**

AWS Student Builder Group — AI/ML Track

[GitHub Profile](https://github.com/mussie56)

---