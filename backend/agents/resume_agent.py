from crewai import Agent,LLM
from llm.llm_client import get_llm
from core.settings import settings

llm = LLM(
        model=f"groq/{settings.GROQ_MODEL}",
        temperature=0.1,
        api_key=settings.GROQ_API_KEY,
    )

def create_resume_agent():
    return Agent(
        role="Resume Analyst",
        goal="Understand resume content and summarize candidate profile",
        backstory="Expert HR analyst specialized in analyzing resumes.",
        llm=llm,
        verbose=True
    )