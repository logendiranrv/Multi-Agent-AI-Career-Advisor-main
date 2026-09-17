from crewai import Agent
from llm.llm_client import get_llm


def create_skill_agent():
    return Agent(
        role="Skill Extraction Specialist",
        goal="Extract technical skills from resume text",
        backstory="Expert at identifying technical skills from resumes.",
        llm=get_llm(),
        verbose=True
    )