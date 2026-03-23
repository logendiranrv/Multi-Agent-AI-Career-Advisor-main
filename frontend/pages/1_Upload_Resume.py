import streamlit as st
import os
from components.api_client import analyze_resume

# ── Load CSS ─────────────────────────────────────────────────
css_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "assets", "styles.css"
)
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Page ─────────────────────────────────────────────────────
st.markdown("# Upload Resume")
st.markdown("Upload a PDF or DOCX file to begin the AI-powered career analysis.")

st.divider()

# ── Upload Section ───────────────────────────────────────────
uploaded_file = st.file_uploader(
    "Select your resume",
    type=["pdf", "docx"],
    help="Supported formats: PDF, DOCX. Maximum file size: 200 MB.",
)

if uploaded_file:
    st.markdown(
        f"""
        <div class="info-header">
            <div>
                <span class="label">File</span><br/>
                <span class="value">{uploaded_file.name}</span>
            </div>
            <div>
                <span class="label">Size</span><br/>
                <span class="value">{uploaded_file.size / 1024:.1f} KB</span>
            </div>
            <div>
                <span class="label">Type</span><br/>
                <span class="value">{uploaded_file.type or "document"}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Analyze Resume", use_container_width=True):
        with st.spinner("Analyzing your resume — this may take a moment..."):
            try:
                result = analyze_resume(uploaded_file)
                st.session_state["analysis_result"] = result

                st.markdown(
                    '<span class="badge badge-success">Analysis complete</span>',
                    unsafe_allow_html=True,
                )

                # ── Quick Summary ────────────────────────────
                st.markdown(
                    f"""
                    <div class="card" style="margin-top:1rem;">
                        <h3>Results Ready</h3>
                        <p>Resume <strong>{result.get("filename", "")}</strong>
                        has been analyzed successfully. Navigate to the pages
                        below to view your full report:</p>
                        <p style="margin-top:0.75rem !important;">
                            <strong>Skill Analysis</strong> &mdash; Extracted skills &amp; gap analysis<br/>
                            <strong>Learning Roadmap</strong> &mdash; Personalized learning plan<br/>
                            <strong>Job Market Insights</strong> &mdash; Market demand data
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            except Exception as e:
                st.error(f"Analysis failed: {e}")

else:
    st.markdown(
        """
        <div class="empty-state">
            <h3>No file selected</h3>
            <p>Drag and drop a resume file above, or click
            <strong>Browse files</strong> to get started.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )