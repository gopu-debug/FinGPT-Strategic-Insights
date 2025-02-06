import streamlit as st
import requests

# 🚨 Hardcoding API Key (Not Recommended for Security) 🚨
HF_API_KEY = "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"

# FinGPT model endpoint on Hugging Face
MODEL_ENDPOINT = "https://api-inference.huggingface.co/models/FinGPT/fingpt-forecaster_dow30_llama2-7b_lora"

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query_fingpt(prompt):
    """Queries the FinGPT model on Hugging Face and returns a response."""
    response = requests.post(
        MODEL_ENDPOINT,
        headers=headers,
        json={"inputs": prompt},
    )
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Streamlit UI
st.set_page_config(page_title="FinGPT Strategic Insights", page_icon="💰", layout="wide")
st.title("💡 FinGPT for Executive Strategy")

st.markdown("""
👋 Welcome! Enter a **strategic management question**, and FinGPT will provide insights.
""")

# User input
query = st.text_area("🔍 Ask a strategic question (e.g., 'How is AI transforming banking?'):")

if st.button("Get Insights"):
    if query.strip():
        with st.spinner("Analyzing..."):
            response = query_fingpt(query)
        st.subheader("📊 FinGPT's Response:")
        st.write(response)
    else:
        st.warning("⚠ Please enter a question before submitting.")
