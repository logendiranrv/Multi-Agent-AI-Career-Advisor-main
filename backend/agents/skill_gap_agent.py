from crewai import Agent,LLM
from llm.llm_client import get_llm
from core.settings import settings

llm = LLM(
        model=f"groq/{settings.GROQ_MODEL}",
        temperature=0.1,
        api_key=settings.GROQ_API_KEY,
    )


def create_gap_agent():
    return Agent(
        role="Skill Gap Analyst",
        goal="Identify missing skills between candidate skills and market demand",
        backstory="Expert career advisor analyzing skill gaps.",
        llm=llm,
        verbose=True
    )