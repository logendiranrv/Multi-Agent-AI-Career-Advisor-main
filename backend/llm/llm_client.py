from core.settings import settings
from crewai import Agent, Task, Crew, Process, LLM


def get_llm():
    """
    Returns a LangChain-compatible ChatGroq LLM instance
    that works with CrewAI agents.
    """

    llm = LLM(
        model=f"groq/{settings.GROQ_MODEL}",
        temperature=0.1,
        api_key=settings.GROQ_API_KEY,
    )

    return llm