import streamlit as st
import os

# ── Load CSS ─────────────────────────────────────────────────
css_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "assets", "styles.css"
)
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Page ─────────────────────────────────────────────────────
st.markdown("# Learning Roadmap")

if "analysis_result" not in st.session_state:
    st.markdown(
        """
        <div class="empty-state">
            <h3>No roadmap generated</h3>
            <p>Upload and analyze a resume first. Navigate to
            <strong>Upload Resume</strong> in the sidebar to begin.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    data = st.session_state["analysis_result"]
    roadmap = data.get("roadmap", "")

    st.markdown("Your personalized learning roadmap based on the skill-gap analysis.")

    st.divider()

    # ── Roadmap content ──────────────────────────────────────
    if roadmap:
        st.markdown(roadmap)
    else:
        st.info("No roadmap data available in the analysis results.")

    # ── Raw output ───────────────────────────────────────────
    with st.expander("View raw output", expanded=False):
        st.code(str(roadmap), language=None)