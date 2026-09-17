from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings using Pydantic."""

    APP_NAME: str = "Multi Agent AI Workflow"
    VERSION: str = "1.0.0"

    # Agent framework mode
    AGENT_FRAMEWORK: str = "crewai"

    # LLM
    GROQ_API_KEY: str
    GROQ_MODEL: str = "llama-3.1-70b-versatile"

    # Search
    SERPER_API_KEY: str = ""

    # Debug
    DEBUG: bool = False

    # File storage
    RESUME_UPLOAD_DIR: str = "data/resumes"

    class Config:
        env_file = ".env"


settings = Settings()