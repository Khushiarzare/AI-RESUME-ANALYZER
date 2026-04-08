import streamlit as st
st.title("AI RESUME ANALYZER")
st.file_uploader("Upload your resume here", type=["pdf", "docx"])
st.divider()

st.sidebar.markdown("<sidebar base='aliceBlue'>Made by [Your Name]</sidebar>", unsafe_allow_html=True)