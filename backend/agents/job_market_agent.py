import os
from dotenv import load_dotenv
from crewai import Agent
from crewai_tools import SerperDevTool
from llm.llm_client import get_llm

load_dotenv()

api = os.getenv("SERPER_API_KEY")
search_tool = SerperDevTool(api_key=api)


def create_market_agent():
    return Agent(
        role="Job Market Analyst",
        goal="Analyze market demand and growth trends for skills found in the resume.",
        backstory="Labor market expert specializing in hiring trends and skill demand across industries.",
        tools=[search_tool],
        llm=get_llm(),
        verbose=True,
        max_iter=2
    )