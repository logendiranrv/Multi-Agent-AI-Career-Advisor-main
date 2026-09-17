from crewai import Agent
from llm.llm_client import get_llm


def create_roadmap_agent():
    return Agent(
        role="Learning Roadmap Planner",
        goal="Generate a step-by-step learning roadmap for missing skills",
        backstory="Expert AI career mentor creating professional learning paths.",
        llm=get_llm(),
        verbose=True
    )