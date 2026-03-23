from crewai import Task
from agents.skill_gap_agent import create_gap_agent


def skill_gap_task():
    agent = create_gap_agent()

    return Task(
        description="""
        Compare the candidate's extracted skills with current market demand.

        Identify:
        - Skills the candidate already has that are in demand
        - Skills the candidate is missing that the market requires
        - Priority level for each missing skill
        """,
        expected_output="List of missing skills with priority levels",
        agent=agent
    )
