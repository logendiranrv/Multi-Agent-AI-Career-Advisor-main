import streamlit as st
import os

# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="CA",
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
    st.markdown("### AI Career Advisor")
    st.caption("Intelligent Resume Analysis Platform  \nv1.0")

# ── Hero ─────────────────────────────────────────────────────
st.markdown("# AI Career Advisor")
st.markdown(
    "Upload your resume and let AI analyze your skills, compare them with "
    "**real job-market demand**, and generate a **personalized learning roadmap** "
    "to accelerate your career growth."
)

st.divider()

# ── Features ─────────────────────────────────────────────────
st.markdown("## Core Capabilities")

cols = st.columns(4, gap="medium")

features = [
    (
        "Resume Parsing",
        "Extract technical and professional skills directly from your resume using AI-powered analysis.",
    ),
    (
        "Market Analysis",
        "Analyze current job-market demand for your skills through AI-driven research.",
    ),
    (
        "Skill Gap Detection",
        "Identify missing skills required for top industry roles and emerging technologies.",
    ),
    (
        "Personalized Roadmap",
        "Generate a structured, prioritized learning plan to close your skill gaps.",
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
            <span class="step-label">AI Extracts Skills</span>
        </div>
        <div class="step-item">
            <span class="step-number">03</span>
            <span class="step-label">Compare with Market</span>
        </div>
        <div class="step-item">
            <span class="step-number">04</span>
            <span class="step-label">Generate Roadmap</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ── Get Started ──────────────────────────────────────────────
st.markdown("## Get Started")

st.markdown(
    """
    <div class="card">
        <p>Use the <strong>sidebar navigation</strong> to begin your analysis.</p>
        <p style="margin-top:0.75rem !important;">
            <strong>Step 1</strong> &mdash; Upload your resume<br/>
            <strong>Step 2</strong> &mdash; View skill analysis<br/>
            <strong>Step 3</strong> &mdash; Explore your learning roadmap<br/>
            <strong>Step 4</strong> &mdash; Check job-market insights
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Footer ───────────────────────────────────────────────────
st.divider()
st.markdown(
    '<div class="footer">AI Career Advisor &mdash; Resume Intelligence Platform</div>',
    unsafe_allow_html=True,
)