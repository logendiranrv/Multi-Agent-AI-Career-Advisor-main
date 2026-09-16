import streamlit as st
import os
import html as html_mod
from components.api_client import check_health

# ── Load CSS ─────────────────────────────────────────────────
css_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "assets", "styles.css"
)
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Sidebar Health Check ─────────────────────────────────────
with st.sidebar:
    st.markdown("### 🤖 AI Career Advisor")
    st.caption("Multi-Agent Intelligence Platform")
    st.markdown("---")
    backend_online = check_health()
    if backend_online:
        st.markdown('<span class="badge badge-success">🟢 Backend Connected</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge badge-error">🔴 Backend Offline</span>', unsafe_allow_html=True)
    st.markdown("---")

# ── Page ─────────────────────────────────────────────────────
st.markdown("# 📊 Skill Analysis")

if "analysis_result" not in st.session_state:
    st.markdown(
        """
        <div class="empty-state">
            <h3>No analysis results available</h3>
            <p>Upload and analyze a resume first to view detailed skill breakdown.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("📤 Go to Upload Resume", use_container_width=True):
        st.switch_page("pages/1_Upload_Resume.py")
else:
    data = st.session_state["analysis_result"]

    # ── Header info ──────────────────────────────────────────
    status_class = "badge-success" if data.get("status") == "success" else "badge-warning"
    status_text = data.get("status", "unknown").capitalize()
    filename = data.get("filename", "—")

    st.markdown(
        f"""
        <div class="info-header">
            <div>
                <span class="label">Analyzed File</span><br/>
                <span class="value">{html_mod.escape(str(filename))}</span>
            </div>
            <div>
                <span class="label">Analysis Status</span><br/>
                <span class="badge {status_class}">{status_text}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ── Skills Analysis Tab & Skill Gap Tab ──────────────────
    tab_skills, tab_gap = st.tabs(["🧩 Extracted Skills", "🎯 Skill Gap Analysis"])

    with tab_skills:
        skills_text = data.get("skills_analysis", "")
        if skills_text:
            st.markdown(skills_text)
            st.download_button(
                label="📥 Download Skills Analysis (.md)",
                data=skills_text,
                file_name=f"skills_analysis_{filename}.md",
                mime="text/markdown",
            )
        else:
            st.info("No skills analysis data available.")

    with tab_gap:
        gap_text = data.get("skill_gap", "")
        if gap_text:
            st.markdown(gap_text)
            st.download_button(
                label="📥 Download Skill Gap Report (.md)",
                data=gap_text,
                file_name=f"skill_gap_{filename}.md",
                mime="text/markdown",
            )
        else:
            st.info("No skill gap data available.")

    # ── Raw output ───────────────────────────────────────────
    with st.expander("🔍 View Raw Output Data", expanded=False):
        st.subheader("Skills Analysis JSON/Text")
        st.code(str(data.get("skills_analysis", "")), language="markdown")
        st.subheader("Skill Gap JSON/Text")
        st.code(str(data.get("skill_gap", "")), language="markdown")