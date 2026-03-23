from crewai import Task
from agents.roadmap_agent import create_roadmap_agent


def roadmap_generation_task():
    agent = create_roadmap_agent()

    return Task(
        description="""
        Create a professional, step-by-step learning roadmap for acquiring
        the missing skills identified in the skill gap analysis.

        Include:
        - Recommended courses and resources
        - Estimated time for each skill
        - Suggested learning order
        """,
        expected_output="Step-by-step learning roadmap with resources and timelines",
        agent=agent
    )