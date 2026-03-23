import streamlit as st
import os
import html as html_mod

# ── Load CSS ─────────────────────────────────────────────────
css_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "assets", "styles.css"
)
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Page ─────────────────────────────────────────────────────
st.markdown("# Skill Analysis")

if "analysis_result" not in st.session_state:
    st.markdown(
        """
        <div class="empty-state">
            <h3>No analysis available</h3>
            <p>Upload and analyze a resume first. Navigate to
            <strong>Upload Resume</strong> in the sidebar to begin.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
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
                <span class="label">File</span><br/>
                <span class="value">{html_mod.escape(str(filename))}</span>
            </div>
            <div>
                <span class="label">Status</span><br/>
                <span class="badge {status_class}">{status_text}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ── Skills Analysis Tab & Skill Gap Tab ──────────────────
    tab_skills, tab_gap = st.tabs(["Extracted Skills", "Skill Gap Analysis"])

    with tab_skills:
        skills_text = data.get("skills_analysis", "")
        if skills_text:
            st.markdown(skills_text)
        else:
            st.info("No skills analysis data available.")

    with tab_gap:
        gap_text = data.get("skill_gap", "")
        if gap_text:
            st.markdown(gap_text)
        else:
            st.info("No skill gap data available.")

    # ── Raw output ───────────────────────────────────────────
    with st.expander("View raw output", expanded=False):
        st.code(str(data.get("skills_analysis", "")), language=None)
        st.code(str(data.get("skill_gap", "")), language=None)