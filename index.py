import streamlit as st
st.title("AI RESUME ANALYZER")
st.file_uploader("Upload your resume here", type=["pdf", "docx"])
st.divider()
import streamlit as st

# Inject custom CSS
st.markdown("""
<style>
.block {
    background-color: #f0f2f6;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin: 10px 0;
    text-align: center;
}

.block h3 {
    color: #333;
}

.block p {
    color: #666;
}
</style>
""", unsafe_allow_html=True)

# Create columns
col1, col2 ,col3 ,col4= st.columns(4)

with col1:
    st.markdown("""
    <div class="block">
        <h5>TOTAL RESUME</h5>
        <p>Content in first column</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="block">
        <h5>ANALYZED CANDIDATES</h5>
        <p>Content in second column</p>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("""
    <div class="block">
        <h5>AVG.MATCH</h5>
        <p>Content in first column</p>
    </div>
    """, unsafe_allow_html=True)


with col4:
    st.markdown("""
    <div class="block">
        <h5>SELECT RESUME</h5>
        <p>Content in first column</p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("<sidebar base='aliceBlue'></sidebar>", unsafe_allow_html=True)
st.sidebar.subheader("DASHBOARD")
st.sidebar.subheader("job posts")
st.sidebar.subheader("Resume Analyzer")
