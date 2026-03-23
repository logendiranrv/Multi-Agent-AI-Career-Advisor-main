from crewai import Task
from agents.skill_agent import create_skill_agent


def skill_extraction_task(resume_text: str):
    agent = create_skill_agent()

    return Task(
        description=f"""
        Extract all technical skills from this resume.

        Resume:
        {resume_text}
        """,
        expected_output="List of extracted technical skills",
        agent=agent
    )