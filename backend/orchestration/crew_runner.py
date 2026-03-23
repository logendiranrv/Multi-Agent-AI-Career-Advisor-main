import os
from groq import Groq
from core.settings import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def run_career_analysis(resume_text: str):
    """
    Directly calling Groq to avoid CrewAI installation issues on Python 3.14
    """

    # Step 1 — Skill Extraction
    skill_prompt = f"Extract all technical skills from this resume: {resume_text}"
    skills_analysis = client.chat.completions.create(
        messages=[{"role": "user", "content": skill_prompt}],
        model=settings.GROQ_MODEL,
    ).choices[0].message.content

    # Step 2 — Market Research
    market_prompt = f"Analyze job market demand for these skills: {skills_analysis}"
    market_analysis = client.chat.completions.create(
        messages=[{"role": "user", "content": market_prompt}],
        model=settings.GROQ_MODEL,
    ).choices[0].message.content

    # Step 3 — Skill Gap Analysis
    gap_prompt = f"Compare these skills: {skills_analysis} against the market demand: {market_analysis}. Identify gaps."
    skill_gap = client.chat.completions.create(
        messages=[{"role": "user", "content": gap_prompt}],
        model=settings.GROQ_MODEL,
    ).choices[0].message.content

    # Step 4 — Roadmap Generation
    roadmap_prompt = f"Generate a learning roadmap based on these skill gaps: {skill_gap}"
    roadmap = client.chat.completions.create(
        messages=[{"role": "user", "content": roadmap_prompt}],
        model=settings.GROQ_MODEL,
    ).choices[0].message.content

    return {
        "skills_analysis": skills_analysis,
        "market_analysis": market_analysis,
        "skill_gap": skill_gap,
        "roadmap": roadmap
    }