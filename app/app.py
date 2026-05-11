import streamlit as st
import spacy
import json

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Load NLP Models
# -----------------------------
nlp = spacy.load("en_core_web_sm")

model = SentenceTransformer('all-MiniLM-L6-v2')


# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="Halluciation_Bias NLP Model",
    layout="wide"
)

# -----------------------------
# App Title
# -----------------------------
st.title(" Hallucination & Bias Detection Model")

st.subheader(
    "Explainable NLP System for Hallucination & Bias Detection"
)

# -----------------------------
# User Input
# -----------------------------
text = st.text_area(
    "Enter AI Generated Text"
)

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("Analyze"):

    # NLP Processing
    doc = nlp(text)

    tokens = []

    for token in doc:

        if not token.is_stop and not token.is_punct:

            tokens.append(token.lemma_)

    # -----------------------------
    # Fact Verification
    # -----------------------------
    claim = text

    fact = "The Eiffel Tower is in Paris"

    claim_embedding = model.encode([claim])

    fact_embedding = model.encode([fact])

    similarity = cosine_similarity(
        claim_embedding,
        fact_embedding
    )[0][0]

    # Fact Classification
    if similarity >= 0.80:

        fact_result = "SUPPORTED"

    elif similarity < 0.40:

        fact_result = "HALLUCINATION"

    else:

        fact_result = "UNCERTAIN"

    # -----------------------------
    # Bias Detection
    # -----------------------------
    bias_phrases = [
        "women are weak",
        "women are emotional",
        "men don't cry"
    ]

    text_lower = text.lower()

    bias_detected = False

    detected_phrase = None

    for phrase in bias_phrases:

        if phrase in text_lower:

            bias_detected = True

            detected_phrase = phrase

            break

    # -----------------------------
    # Final Report
    # -----------------------------
    final_report = {

        "Input Text": text,

        "Processed Tokens": tokens,

        "Fact Verification": fact_result,

        "Similarity Score": float(similarity),

        "Bias Detected": bias_detected,

        "Bias Phrase": detected_phrase,

        "Explanation":
        "Potential hallucination and stereotype analysis completed."
    }

    # -----------------------------
    # Display Results
    # -----------------------------
    st.success("Analysis Completed")

    st.write(final_report)

    st.json(final_report)

    # -----------------------------
    # Download JSON Report
    # -----------------------------
    report_json = json.dumps(
        final_report,
        indent=4
    )

    st.download_button(
        label="Download Report",
        data=report_json,
        file_name="truthguard_report.json",
        mime="application/json"
    )