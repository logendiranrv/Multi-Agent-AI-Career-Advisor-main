from crewai import Agent,LLM
from llm.llm_client import get_llm
from core.settings import settings

llm = LLM(
        model=f"groq/{settings.GROQ_MODEL}",
        temperature=0.1,
        api_key=settings.GROQ_API_KEY,
    )
def create_roadmap_agent():
    return Agent(
        role="Learning Roadmap Planner",
        goal="Generate a step-by-step learning roadmap for missing skills",
        backstory="Expert AI career mentor creating professional learning paths.",
        llm=llm,
        verbose=True
    )