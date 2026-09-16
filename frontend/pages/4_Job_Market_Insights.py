import streamlit as st
import pandas as pd
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
st.markdown("# 📈 Job Market Insights")

if "analysis_result" not in st.session_state:
    st.markdown(
        """
        <div class="empty-state">
            <h3>No custom market analysis available yet</h3>
            <p>Upload your resume to trigger real-time web research on skill demand.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("📤 Go to Upload Resume", use_container_width=True):
        st.switch_page("pages/1_Upload_Resume.py")

    st.divider()
    st.markdown("#### 📊 Sample Tech Market Demand Overview")
    st.caption("The chart below illustrates sample industry demand benchmarks. Run a resume analysis to see targeted insights.")

    SAMPLE_DATA = {
        "Skill": [
            "Python", "Generative AI", "Machine Learning", "Cloud (AWS/GCP)",
            "Cybersecurity", "Data Engineering", "DevOps/Kubernetes", "System Design",
        ],
        "Demand Score": [95, 93, 91, 88, 84, 82, 79, 76],
        "YoY Growth (%)": [12, 45, 18, 15, 22, 14, 11, 10],
    }
    df = pd.DataFrame(SAMPLE_DATA).sort_values("Demand Score", ascending=False)

    try:
        import plotly.express as px

        fig = px.bar(
            df, x="Skill", y="Demand Score",
            color="Demand Score",
            color_continuous_scale=["#1E3A5F", "#3B82F6", "#60A5FA"],
            text_auto=True,
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

    st.markdown(
        f"""
        <div class="info-header">
            <div>
                <span class="label">Source Resume</span><br/>
                <span class="value">{html_mod.escape(str(filename))}</span>
            </div>
            <div>
                <span class="label">Research Status</span><br/>
                <span class="badge badge-success">Live Market Research</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ── Market Analysis Content ──────────────────────────────
    if market_text:
        st.markdown(market_text)
        st.divider()
        st.download_button(
            label="📥 Download Market Research Insights (.md)",
            data=market_text,
            file_name=f"market_insights_{filename}.md",
            mime="text/markdown",
        )
    else:
        st.info("No market analysis data returned from the backend.")

    # ── Raw output ───────────────────────────────────────────
    with st.expander("🔍 View Raw Market Research Text", expanded=False):
        st.code(str(market_text), language="markdown")