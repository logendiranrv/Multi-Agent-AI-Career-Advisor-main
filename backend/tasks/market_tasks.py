from crewai import Task
from agents.job_market_agent import create_market_agent



def market_research_task():

    agent = create_market_agent()

    return Task(
        description="""
Analyze the job market demand for the skills extracted from the resume.

Provide a detailed explanation including:

1. The most valuable skills from the resume
2. Market demand for those skills
3. Industry hiring trends
4. Future growth opportunities
5. Which skills are most valuable for career growth

Limit the analysis to the top 8 most important skills.
""",
        agent=agent,
        expected_output="Detailed job market analysis report"
    )