SKILL_EXTRACTION_PROMPT = """
Extract all technical skills from the following resume.

Return skills as a list.

Resume:
{resume_text}
"""


JOB_MARKET_ANALYSIS_PROMPT = """
Analyze current job market demand for the following skills.

Skills:
{skills}

Return:
- In demand skills
- Future skills
"""


SKILL_GAP_PROMPT = """
Compare user skills with market demand.

User Skills:
{user_skills}

Market Skills:
{market_skills}

Return missing skills.
"""


ROADMAP_PROMPT = """
Create a learning roadmap to acquire these skills.

Missing Skills:
{missing_skills}

Return a step-by-step roadmap.
"""