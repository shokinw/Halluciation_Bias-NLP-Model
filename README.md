# TruthGuard AI

## Explainable NLP System for Hallucination & Bias Detection

TruthGuard AI is an advanced NLP + Explainable AI project designed to detect hallucinations, misinformation, and biased language in AI-generated text.

The system combines:

* NLP preprocessing
* Sentence-BERT embeddings
* Semantic similarity verification
* Bias & stereotype detection
* Explainable AI (SHAP/LIME)
* Streamlit interactive dashboard

This project is built as a professional placement-level NLP system using Python, Hugging Face, spaCy, Scikit-learn, and Streamlit.

---

# Project Objective

Large Language Models (LLMs) can sometimes:

* Generate false information (hallucinations)
* Produce biased or stereotypical outputs
* Provide misleading factual statements

TruthGuard AI helps solve this problem by:

1. Verifying factual correctness
2. Detecting biased language
3. Explaining WHY the output was flagged
4. Generating interpretable AI audit reports

---

# Features

## Hallucination Detection

* Detects incorrect factual statements
* Uses Sentence-BERT semantic embeddings
* Uses cosine similarity for fact verification

## Bias Detection

* Detects gender stereotypes
* Detects harmful phrases
* Detects biased language patterns

## Explainable AI

* Uses SHAP/LIME for model explainability
* Highlights influential words
* Improves AI transparency

## Interactive Dashboard

* Streamlit-based frontend
* Real-time text analysis
* Displays hallucination & bias scores

## Visualization & Evaluation

* Confusion Matrix
* Similarity Score Graphs
* Bias Score Charts
* Dataset Distribution Analysis

---

# Tech Stack

| Purpose              | Technology                |
| -------------------- | ------------------------- |
| Programming Language | Python                    |
| IDE                  | VS Code                   |
| Notebook             | Jupyter Notebook          |
| NLP Framework        | spaCy                     |
| Embeddings           | Sentence-BERT             |
| Transformers         | Hugging Face Transformers |
| Machine Learning     | Scikit-learn              |
| Visualization        | Matplotlib, Seaborn       |
| Explainability       | SHAP, LIME                |
| Frontend             | Streamlit                 |

---

# Project Architecture

```text
Input Text
   ↓
Preprocessing
   ↓
Tokenization & Lemmatization
   ↓
Fact Extraction
   ↓
Sentence-BERT Embeddings
   ↓
Cosine Similarity
   ↓
Hallucination Detection
   ↓
Bias Detection
   ↓
Explainability
   ↓
Final AI Audit Report
```

---

# Folder Structure

```text
TruthGuardAI/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_embeddings.ipynb
│   ├── 05_fact_verification.ipynb
│   ├── 06_bias_detection.ipynb
│   ├── 07_explainability.ipynb
│   ├── 08_model_evaluation.ipynb
│   └── 09_final_pipeline.ipynb
│
├── app/
│   └── app.py
│
├── models/
│
├── outputs/
│   ├── charts/
│   ├── predictions/
│   └── reports/
│
├── utils/
│   ├── preprocessing.py
│   ├── verification.py
│   ├── bias_detection.py
│   └── visualization.py
│
├── requirements.txt
└── README.md
```

---

# Dataset Used

## 1. TruthfulQA

Purpose:

* Hallucination detection
* Truthfulness evaluation

## 2. BOLD Dataset

Purpose:

* Bias detection
* Stereotype analysis

## 3. FEVER / FEVEROUS

Purpose:

* Fact verification
* Semantic reasoning

---

# Installation Guide

## Step 1 — Clone Repository

```bash
git clone <your-repository-link>
cd TruthGuardAI
```

---

## Step 2 — Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

# Register Jupyter Kernel

```bash
python -m ipykernel install --user --name=truthguard
```

---

# Running Jupyter Notebooks

Open VS Code.

Install extensions:

* Python
* Jupyter
* Pylance

Then open notebooks and select kernel:

```text
truthguard
```

---

# Running Streamlit App

Move to project directory:

```bash
cd app
```

Run:

```bash
streamlit run app.py
```

The browser will automatically open.

---

# Example Input

```text
The Eiffel Tower is in London and women are weak.
```

---

# Example Output

```json
{
  "fact_check": "Hallucination",
  "similarity_score": 0.34,
  "bias_detected": true,
  "bias_phrase": "women are weak",
  "explanation": "Location incorrect and gender stereotype detected"
}
```

---

# Model Workflow

## Step 1 — Preprocessing

* Lowercasing
* Tokenization
* Stopword removal
* Lemmatization

## Step 2 — Embedding Generation

Sentence-BERT converts text into semantic vectors.

## Step 3 — Semantic Verification

Cosine similarity compares AI-generated claims with verified facts.

## Step 4 — Bias Detection

Rule-based + NLP-based stereotype detection.

## Step 5 — Explainability

SHAP/LIME highlights why predictions were made.

---

# Visualizations Included

* Label Distribution Graphs
* Pie Charts
* Similarity Score Charts
* Bias Score Graphs
* Confusion Matrix Heatmaps

---

# Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

# Professional Concepts Used

| NLP Concept       | Usage                      |
| ----------------- | -------------------------- |
| Tokenization      | Split text into words      |
| Lemmatization     | Convert words to root form |
| Embeddings        | Semantic understanding     |
| SBERT             | Sentence representation    |
| Cosine Similarity | Fact verification          |
| Bias Detection    | Ethical AI                 |
| Explainable AI    | Transparent predictions    |

---

# Future Improvements

* Transformer-based bias classifier
* Multi-hop fact verification
* Knowledge Graph integration
* Real-time API deployment
* Hugging Face Spaces deployment
* Docker containerization
* CI/CD pipelines
* GPU optimization
* Fine-tuning custom transformers

---

# Use Cases

* AI Safety Systems
* LLM Monitoring
* Fake News Detection
* Ethical AI Auditing
* Educational AI Systems
* Content Moderation
* Research Applications

---

# Placement Interview Explanation

## Problem

Large Language Models often generate hallucinated or biased outputs.

## Solution

TruthGuard AI verifies semantic correctness using Sentence-BERT embeddings and detects harmful stereotypes using bias detection techniques.

## Outcome

The system generates explainable AI audit reports with semantic verification scores and bias analysis.

---

# Author

Samridhi Sharma

B.Tech CSE (AI & ML)

NLP | AI | Machine Learning | Explainable AI

---

# License

This project is developed for educational and research purposes.
