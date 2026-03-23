import traceback
from fastapi import FastAPI, UploadFile, File, HTTPException
from core.settings import settings
from services.file_storage import save_uploaded_file
from services.resume_parser import extract_resume_text
from orchestration.crew_runner import run_career_analysis

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Multi-Agent AI Career Workflow System",
)


@app.get("/")
def root():
    return {
        "message": "Multi-Agent AI Workflow API Running",
        "framework_mode": settings.AGENT_FRAMEWORK
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        print(f"DEBUG: Starting analysis for {file.filename}")
        file_path = save_uploaded_file(file)
        print(f"DEBUG: File saved to {file_path}")

        resume_text = extract_resume_text(file_path)
        print(f"DEBUG: Extracted text length: {len(resume_text)}")

        analysis = run_career_analysis(resume_text)
        print(f"DEBUG: Analysis completed")

        return {
            "status": "success",
            "filename": file.filename,
            "skills_analysis": analysis["skills_analysis"],
            "skill_gap": analysis["skill_gap"],
            "roadmap": analysis["roadmap"],
            "market_analysis": analysis["market_analysis"]
        }
    except Exception as e:
        error_msg = traceback.format_exc()
        print(f"ERROR level: {error_msg}")
        with open("error_trace.log", "a") as f:
            f.write(f"\n--- ERROR AT {settings.VERSION} ---\n{error_msg}\n")
        raise HTTPException(status_code=500, detail=str(e))