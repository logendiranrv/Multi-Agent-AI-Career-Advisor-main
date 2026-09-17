from crewai import Agent
from llm.llm_client import get_llm


def create_resume_agent():
    return Agent(
        role="Resume Analyst",
        goal="Understand resume content and summarize candidate profile",
        backstory="Expert HR analyst specialized in analyzing resumes.",
        llm=get_llm(),
        verbose=True
    )