import streamlit as st
import os
from components.api_client import check_health

# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load CSS ─────────────────────────────────────────────────
css_path = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🤖 AI Career Advisor")
    st.caption("Multi-Agent Intelligence Platform  \nv1.0")
    
    st.markdown("---")
    backend_online = check_health()
    if backend_online:
        st.markdown('<span class="badge badge-success">🟢 Backend Connected</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge badge-error">🔴 Backend Offline</span>', unsafe_allow_html=True)
        st.caption("Please start backend server (`uvicorn main:app`).")
    st.markdown("---")

# ── Hero ─────────────────────────────────────────────────────
st.markdown("# 🚀 AI-Powered Career Advisor")
st.markdown(
    "Upload your resume and let our autonomous **CrewAI multi-agent system** analyze your technical skills, "
    "cross-reference them with **live job-market demand**, and generate a **personalized learning roadmap** "
    "to fast-track your career."
)

st.divider()

# ── Metrics / Stats ──────────────────────────────────────────
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
with m_col1:
    st.markdown(
        '<div class="kpi-card"><p class="kpi-value">4</p><p class="kpi-label">Autonomous Agents</p></div>',
        unsafe_allow_html=True,
    )
with m_col2:
    st.markdown(
        '<div class="kpi-card"><p class="kpi-value">100%</p><p class="kpi-label">Automated Analysis</p></div>',
        unsafe_allow_html=True,
    )
with m_col3:
    st.markdown(
        '<div class="kpi-card"><p class="kpi-value">Groq 70B</p><p class="kpi-label">LLM Intelligence</p></div>',
        unsafe_allow_html=True,
    )
with m_col4:
    st.markdown(
        '<div class="kpi-card"><p class="kpi-value">Real-time</p><p class="kpi-label">Market Insights</p></div>',
        unsafe_allow_html=True,
    )

st.divider()

# ── Features ─────────────────────────────────────────────────
st.markdown("## Core Capabilities")

cols = st.columns(4, gap="medium")

features = [
    (
        "📄 Resume Parsing",
        "Extract technical and professional skills directly from your PDF/DOCX resume using AI.",
    ),
    (
        "📊 Market Analysis",
        "Analyze current job-market demand for your skills through AI web research.",
    ),
    (
        "🎯 Skill Gap Detection",
        "Identify missing critical skills required for top industry roles.",
    ),
    (
        "🗺️ Personalized Roadmap",
        "Generate a structured, phased learning plan with resources to close your skill gaps.",
    ),
]

for col, (title, desc) in zip(cols, features):
    with col:
        st.markdown(
            f"""
            <div class="feature-card">
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# ── How It Works ─────────────────────────────────────────────
st.markdown("## How It Works")

st.markdown(
    """
    <div class="step-bar">
        <div class="step-item">
            <span class="step-number">01</span>
            <span class="step-label">Upload Resume</span>
        </div>
        <div class="step-item">
            <span class="step-number">02</span>
            <span class="step-label">AI Agent Analysis</span>
        </div>
        <div class="step-item">
            <span class="step-number">03</span>
            <span class="step-label">Market Research</span>
        </div>
        <div class="step-item">
            <span class="step-number">04</span>
            <span class="step-label">Actionable Roadmap</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ── CTA ─────────────────────────────────────────────────────
st.markdown("## Get Started Now")

cta_col1, cta_col2 = st.columns([2, 1])
with cta_col1:
    st.markdown(
        """
        <div class="card">
            <h3>Ready to analyze your resume?</h3>
            <p>Upload your resume file (PDF or DOCX) to get a full multi-agent career assessment in minutes.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with cta_col2:
    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
    if st.button("📤 Go to Upload Resume", use_container_width=True):
        st.switch_page("pages/1_Upload_Resume.py")

# ── Footer ───────────────────────────────────────────────────
st.divider()
st.markdown(
    '<div class="footer">AI Career Advisor &mdash; Multi-Agent AI Workflow System</div>',
    unsafe_allow_html=True,
)