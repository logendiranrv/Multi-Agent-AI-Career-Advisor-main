from crewai import Agent,LLM
from llm.llm_client import get_llm
from core.settings import settings


llm = LLM(
        model=f"groq/{settings.GROQ_MODEL}",
        temperature=0.1,
        api_key=settings.GROQ_API_KEY,
    )

def create_skill_agent():
    return Agent(
        role="Skill Extraction Specialist",
        goal="Extract technical skills from resume text",
        backstory="Expert at identifying technical skills from resumes.",
        llm=llm,
        verbose=True
    )