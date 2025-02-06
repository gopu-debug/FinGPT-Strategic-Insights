import os
import streamlit as st
import requests




# ✅ Use the latest FinGPT model
MODEL_ENDPOINT = "https://api-inference.huggingface.co/models/FinGPT/fingpt-mt_llama3-8b_lora"

# Replace with your working Hugging Face API Key
HF_API_KEY = "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"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def query_fingpt(prompt):
    """Queries FinGPT on Hugging Face"""
    response = requests.post(
        MODEL_ENDPOINT,
        headers=headers,
        json={"inputs": prompt},
    )
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    elif response.status_code == 404:
        return "🚨 Model not found. Try using a different FinGPT model."
    else:
        return f"🚨 Error: {response.status_code}, {response.text}"

# ✅ Ensure `MODEL_ENDPOINT` is defined BEFORE calling query_fingpt()
st.set_page_config(page_title="FinGPT Strategic Insights", page_icon="💰", layout="wide")
st.title("💡 FinGPT for Executive Strategy")

st.markdown("""
👋 Welcome! Enter a **strategic management question**, and FinGPT will provide insights.
""")

# ✅ Ensure query is collected before calling query_fingpt()
query = st.text_area("🔍 Ask a strategic question (e.g., 'How is AI transforming banking?'):")

if st.button("Get Insights"):
    if query.strip():
        with st.spinner("Analyzing..."):
            response = query_fingpt(query)  # ✅ Now using `fingpt-mt_llama3-8b_lora`
        st.subheader("📊 FinGPT's Response:")
        st.write(response)
    else:
        st.warning("⚠ Please enter a question before submitting.")
