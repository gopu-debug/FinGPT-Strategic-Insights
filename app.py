import os
import subprocess
import streamlit as st

# Install FinNLP manually if not present
if not os.path.exists("FinNLP"):
    subprocess.run(["git", "clone", "https://github.com/AI4Finance-Foundation/FinNLP.git"])
    subprocess.run(["pip", "install", "-e", "FinNLP"])

# Import after installation
from finnlp.models.llm.fingpt_api import FinGPT_API

# Initialize FinGPT
fingpt = FinGPT_API()

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
            response = fingpt.chat(query)
        st.subheader("📊 FinGPT's Response:")
        st.write(response)
    else:
        st.warning("⚠ Please enter a question before submitting.")
