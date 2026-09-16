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
st.markdown("# 🗺️ Personalized Learning Roadmap")

if "analysis_result" not in st.session_state:
    st.markdown(
        """
        <div class="empty-state">
            <h3>No roadmap available</h3>
            <p>Upload and analyze a resume first to generate your phased learning plan.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("📤 Go to Upload Resume", use_container_width=True):
        st.switch_page("pages/1_Upload_Resume.py")
else:
    data = st.session_state["analysis_result"]
    roadmap = data.get("roadmap", "")
    filename = data.get("filename", "—")

    st.markdown(
        f"""
        <div class="info-header">
            <div>
                <span class="label">Candidate File</span><br/>
                <span class="value">{html_mod.escape(str(filename))}</span>
            </div>
            <div>
                <span class="label">Plan Type</span><br/>
                <span class="badge badge-success">Phased Learning Roadmap</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ── Roadmap content ──────────────────────────────────────
    if roadmap:
        st.markdown(roadmap)
        st.divider()
        st.download_button(
            label="📥 Download Personalized Roadmap (.md)",
            data=roadmap,
            file_name=f"learning_roadmap_{filename}.md",
            mime="text/markdown",
        )
    else:
        st.info("No roadmap data available in the analysis results.")

    # ── Raw output ───────────────────────────────────────────
    with st.expander("🔍 View Raw Roadmap Markdown", expanded=False):
        st.code(str(roadmap), language="markdown")