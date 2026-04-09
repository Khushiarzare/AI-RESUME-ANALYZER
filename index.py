import streamlit as st

# Page config
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #f5f7fb;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background:  linear-gradient(180deg, #141E30, #243B55);
    color: white;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Card styling */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

/* Metric card */
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
}

/* Header */
.header {
    font-size: 28px;
    font-weight: bold;
    color: #333;
}

/* Sub text */
.subtext {
    color: gray;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.title("⚙ AI Resume Analyzer")


menu = st.sidebar.radio("", [
    "Dashboard",
    "Resume Analyzer",
    "Job Postings",
    "Analytics",
    "Settings"
])

st.sidebar.markdown("---")


# ------------------ HEADER ------------------
st.markdown('<div class="header">AI Resume Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">AI-powered recruitment insights and candidate analysis</div>', unsafe_allow_html=True)

st.markdown("")

# ------------------ DEMO BOX ------------------
st.markdown("""
<div class="card">
<ul>
<li>✔ Interactive demo</li>
<li>✔ Mock analysis results</li>
<li>✔ File upload simulation</li>
<li>✔ Charts & insights</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("")

# ------------------ METRICS ------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h2>2</h2>
        <p>Total Resumes</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h2>2</h2>
        <p>Analyzed Candidates</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h2>90%</h2>
        <p>Avg Match Score</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h2>12 Days</h2>
        <p>Avg Processing Time</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# ------------------ CHART / DATA SECTION ------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h4>📊 Resume Analysis</h4></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h4>📈 Candidate Growth</h4></div>', unsafe_allow_html=True)

# ------------------ FOOTER ------------------

