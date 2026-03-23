import os
from dotenv import load_dotenv
from crewai import Agent,LLM
from crewai_tools import SerperDevTool
from llm.llm_client import get_llm
from core.settings import settings

load_dotenv()

llm = LLM(
        model=f"groq/{settings.GROQ_MODEL}",
        temperature=0.1,
        api_key=settings.GROQ_API_KEY,
    )

api = os.getenv("SERPER_API_KEY")
search_tool = SerperDevTool(api_key=api)

def create_market_agent():
    return Agent(
        role="Job Market Analyst",
        goal="Analyze market demand and growth trends for skills found in the resume.",
        backstory="Labor market expert specializing in hiring trends and skill demand across industries.",
        tools=[search_tool],
        llm=llm,
        verbose=True,
        max_iter=2
    )