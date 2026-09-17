from crewai import Agent
from llm.llm_client import get_llm


def create_gap_agent():
    return Agent(
        role="Skill Gap Analyst",
        goal="Identify missing skills between candidate skills and market demand",
        backstory="Expert career advisor analyzing skill gaps.",
        llm=get_llm(),
        verbose=True
    )