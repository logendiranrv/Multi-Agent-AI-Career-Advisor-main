import streamlit as st
import pandas as pd
import os

# ── Load CSS ─────────────────────────────────────────────────
css_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "assets", "styles.css"
)
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Page ─────────────────────────────────────────────────────
st.markdown("# Job Market Insights")

if "analysis_result" not in st.session_state:
    st.markdown(
        """
        <div class="empty-state">
            <h3>No market analysis available</h3>
            <p>Upload and analyze a resume first. Navigate to
            <strong>Upload Resume</strong> in the sidebar to begin.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()
    st.markdown("#### Sample Market Overview")
    st.caption("The data below is a static sample. Run a resume analysis to see personalized insights.")

    SAMPLE_DATA = {
        "Skill": [
            "Python", "Machine Learning", "Cloud Computing",
            "Cybersecurity", "Data Engineering", "DevOps",
            "Generative AI", "Kubernetes",
        ],
        "Demand Score": [95, 91, 88, 84, 82, 79, 93, 76],
        "YoY Growth (%)": [12, 18, 15, 22, 14, 10, 45, 11],
    }
    df = pd.DataFrame(SAMPLE_DATA).sort_values("Demand Score", ascending=False)

    try:
        import plotly.express as px

        fig = px.bar(
            df, x="Skill", y="Demand Score",
            color="Demand Score",
            color_continuous_scale=["#1E3A5F", "#3B82F6", "#60A5FA"],
        )
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#94A3B8",
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor="#1E2D4A"),
            coloraxis_showscale=False,
            margin=dict(l=0, r=0, t=20, b=0),
            height=380,
        )
        st.plotly_chart(fig, use_container_width=True)
    except ImportError:
        st.bar_chart(df.set_index("Skill")["Demand Score"])

else:
    data = st.session_state["analysis_result"]
    market_text = data.get("market_analysis", "")
    filename = data.get("filename", "—")

    st.markdown("Personalized job market analysis based on your resume.")

    # ── Header ───────────────────────────────────────────────
    st.markdown(
        f"""
        <div class="info-header">
            <div>
                <span class="label">Source</span><br/>
                <span class="value">{filename}</span>
            </div>
            <div>
                <span class="label">Type</span><br/>
                <span class="badge badge-success">Live Analysis</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ── Market Analysis Content ──────────────────────────────
    if market_text:
        st.markdown(market_text)
    else:
        st.info("No market analysis data returned from the backend.")

    # ── Raw output ───────────────────────────────────────────
    with st.expander("View raw output", expanded=False):
        st.code(str(market_text), language=None)