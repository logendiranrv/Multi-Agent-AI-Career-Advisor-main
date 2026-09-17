from core.settings import settings
from crewai import Agent, Task, Crew, Process, LLM


def get_llm():
    """
    Returns a CrewAI LLM instance configured for Groq.
    """
    model_name = settings.GROQ_MODEL.strip()
    if not model_name.startswith("groq/"):
        model_name = f"groq/{model_name}"

    return LLM(
        model=model_name,
        temperature=0.1,
        api_key=settings.GROQ_API_KEY,
    )