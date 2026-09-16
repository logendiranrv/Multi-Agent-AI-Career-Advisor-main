import streamlit as st
import os
from components.api_client import analyze_resume, check_health

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
st.markdown("# 📤 Upload Resume")
st.markdown("Upload your resume in PDF or DOCX format to trigger our autonomous multi-agent analysis.")

st.divider()

if not backend_online:
    st.warning("⚠️ **Backend Server Offline**: Please ensure the backend server is running before attempting resume analysis.")

# ── Upload Section ───────────────────────────────────────────
uploaded_file = st.file_uploader(
    "Select your resume file",
    type=["pdf", "docx"],
    help="Supported formats: PDF, DOCX. Maximum file size: 20 MB.",
)

if uploaded_file:
    st.markdown(
        f"""
        <div class="info-header">
            <div>
                <span class="label">File Name</span><br/>
                <span class="value">{uploaded_file.name}</span>
            </div>
            <div>
                <span class="label">File Size</span><br/>
                <span class="value">{uploaded_file.size / 1024:.1f} KB</span>
            </div>
            <div>
                <span class="label">Format</span><br/>
                <span class="value">{(uploaded_file.name.split('.')[-1]).upper()}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("✨ Analyze Resume with AI Agents", use_container_width=True, disabled=not backend_online):
        with st.spinner("🤖 Multi-agent team working: Extracting skills, analyzing market, identifying gaps & building roadmap... (This takes ~30-60 seconds)"):
            try:
                result = analyze_resume(uploaded_file)
                st.session_state["analysis_result"] = result

                st.markdown(
                    '<span class="badge badge-success">✅ Analysis Complete</span>',
                    unsafe_allow_html=True,
                )

                st.markdown(
                    f"""
                    <div class="card" style="margin-top:1rem;">
                        <h3>🎉 Analysis Successfully Completed!</h3>
                        <p>Resume <strong>{result.get("filename", "")}</strong> has been processed by our AI agents. Explore your custom report:</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("📊 View Skill Analysis", use_container_width=True):
                        st.switch_page("pages/2_Skill_Analysis.py")
                with col2:
                    if st.button("🗺️ View Learning Roadmap", use_container_width=True):
                        st.switch_page("pages/3_Learning_Roadmap.py")
                with col3:
                    if st.button("📈 View Job Market Insights", use_container_width=True):
                        st.switch_page("pages/4_Job_Market_Insights.py")

            except Exception as e:
                st.error(f"❌ Analysis failed: {e}")

else:
    st.markdown(
        """
        <div class="empty-state">
            <h3>No file selected</h3>
            <p>Drag and drop a PDF or DOCX resume file above, or click <strong>Browse files</strong> to begin.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )