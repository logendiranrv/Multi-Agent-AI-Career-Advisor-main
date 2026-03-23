# Multi-Agent AI Career Advisor

An AI-powered resume intelligence platform that analyzes resumes, identifies skill gaps against current market demand, and generates personalized learning roadmaps. Built with a multi-agent architecture using CrewAI, FastAPI, and Streamlit.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Environment Variables](#environment-variables)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [Frontend Pages](#frontend-pages)
- [Tech Stack](#tech-stack)

---

## Overview

The platform processes a resume through a sequential multi-agent pipeline:

1. **Skill Extraction** -- Parses the resume and identifies technical, procedural, and certified skills.
2. **Job Market Research** -- Analyzes current market demand for the extracted skills using web search.
3. **Skill Gap Analysis** -- Compares the candidate's skills against market demand and assigns priority levels.
4. **Roadmap Generation** -- Produces a phased learning plan with courses, timelines, and resources.

Each stage is handled by a dedicated AI agent, orchestrated sequentially via CrewAI.

---

## Architecture

```
                        +-------------------+
                        |   Streamlit UI    |
                        |   (Frontend)      |
                        +---------+---------+
                                  |
                             HTTP POST
                                  |
                        +---------v---------+
                        |   FastAPI Server  |
                        |   (Backend)       |
                        +---------+---------+
                                  |
                    +-------------+-------------+
                    |                             |
              +-----v------+              +------v------+
              | File Store |              | Resume      |
              | (PDF/DOCX) |              | Parser      |
              +------------+              +------+------+
                                                 |
                                          +------v------+
                                          | CrewAI      |
                                          | Orchestrator|
                                          +------+------+
                                                 |
                    +----------+---------+-------+--------+
                    |          |         |                 |
               +----v---+ +---v----+ +--v-----+  +-------v----+
               | Skill  | | Market | | Gap    |  | Roadmap    |
               | Agent  | | Agent  | | Agent  |  | Agent      |
               +--------+ +--------+ +--------+  +------------+
                    |          |
                 Groq LLM   Groq LLM + Serper Search
```

---

## Project Structure

```
multi_agent_ai/
|
+-- backend/
|   +-- main.py                          # FastAPI application entry point
|   +-- requirements.txt                 # Python dependencies
|   +-- core/
|   |   +-- settings.py                  # Pydantic settings & env config
|   +-- agents/
|   |   +-- resume_agent.py              # Resume parsing agent
|   |   +-- skill_agent.py               # Skill extraction agent
|   |   +-- job_market_agent.py          # Job market research agent
|   |   +-- skill_gap_agent.py           # Skill gap analysis agent
|   |   +-- roadmap_agent.py             # Roadmap generation agent
|   +-- tasks/
|   |   +-- skill_tasks.py              # Skill extraction task definition
|   |   +-- market_tasks.py             # Market research task definition
|   |   +-- gap_tasks.py                # Skill gap task definition
|   |   +-- roadmap_tasks.py            # Roadmap generation task definition
|   +-- orchestration/
|   |   +-- crew_runner.py              # CrewAI pipeline orchestrator
|   +-- llm/
|   |   +-- llm_client.py              # Groq LLM client configuration
|   |   +-- prompts.py                 # Prompt templates
|   +-- services/
|   |   +-- file_storage.py            # Resume file upload & storage
|   |   +-- resume_parser.py           # PDF/DOCX text extraction
|   +-- data/
|       +-- resumes/                   # Uploaded resume files
|
+-- frontend/
    +-- app.py                          # Streamlit app entry point (home page)
    +-- .streamlit/
    |   +-- config.toml                 # Streamlit theme configuration
    +-- assets/
    |   +-- styles.css                  # Custom CSS design system
    +-- components/
    |   +-- api_client.py               # Backend API client with error handling
    +-- pages/
        +-- 1_Upload_Resume.py          # Resume upload page
        +-- 2_Skill_Analysis.py         # Skills & gap analysis display
        +-- 3_Learning_Roadmap.py       # Personalized roadmap display
        +-- 4_Job_Market_Insights.py    # Market analysis display
```

---

## Prerequisites

- Python 3.10 or higher
- A [Groq](https://console.groq.com/) API key (free tier available)
- A [Serper](https://serper.dev/) API key for web search (free tier available)

---

## Environment Variables

Create a `.env` file inside the `backend/` directory:

```env
# Required -- Groq LLM
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama3-70b-8192

# Required -- Web search for market research agent
SERPER_API_KEY=your_serper_api_key_here

# Optional
DEBUG=false
```

| Variable         | Required | Default              | Description                                    |
|------------------|----------|----------------------|------------------------------------------------|
| `GROQ_API_KEY`   | Yes      | --                   | API key from Groq console                      |
| `GROQ_MODEL`     | No       | `llama3-70b-8192`    | Groq model identifier                          |
| `SERPER_API_KEY`  | Yes      | --                   | API key from Serper for web search              |
| `DEBUG`          | No       | `false`              | Enable debug logging                           |

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd multi_agent_ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install backend dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Install frontend dependencies

```bash
pip install streamlit plotly pandas requests
```

### 5. Configure environment variables

```bash
cp backend/.env.example backend/.env
# Edit backend/.env with your API keys
```

---

## Running the Application

You need two terminals -- one for the backend API and one for the frontend.

### Terminal 1 -- Backend API

```bash
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`. Verify with:

```
GET http://localhost:8000/health
```

### Terminal 2 -- Frontend

```bash
cd frontend
streamlit run app.py
```

The UI will open at `http://localhost:8501`.

---

## API Reference

### `GET /`

Returns API status and framework mode.

### `GET /health`

Health check endpoint. Returns `{"status": "healthy"}`.

### `POST /analyze`

Upload a resume for full analysis.

**Request:** `multipart/form-data` with a `file` field (PDF or DOCX).

**Response:**

```json
{
    "status": "success",
    "filename": "resume.pdf",
    "skills_analysis": "Extracted skills with categorization...",
    "market_analysis": "Job market demand analysis...",
    "skill_gap": "Missing skills with priority levels...",
    "roadmap": "Phased learning roadmap with resources..."
}
```

---

## Frontend Pages

| Page                    | Description                                                     |
|-------------------------|-----------------------------------------------------------------|
| Home                    | Platform overview, feature summary, and navigation guide        |
| Upload Resume           | File upload (PDF/DOCX) with metadata display and analysis trigger |
| Skill Analysis          | Two-tab view showing extracted skills and skill gap analysis     |
| Learning Roadmap        | Phased, prioritized learning plan with courses and timelines    |
| Job Market Insights     | Market demand analysis; sample chart when no data is available  |

---

## Tech Stack

| Layer         | Technology                                                  |
|---------------|-------------------------------------------------------------|
| LLM           | Groq (Llama 3 70B) via `langchain-groq`                    |
| Agent Framework | CrewAI with sequential process orchestration              |
| Web Search    | Serper API via `crewai-tools`                               |
| Backend API   | FastAPI + Uvicorn                                           |
| Resume Parsing | pdfplumber (PDF), python-docx (DOCX)                       |
| Frontend      | Streamlit with custom CSS design system                     |
| Charts        | Plotly Express                                              |
| Configuration | Pydantic Settings with `.env` file support                  |

---

## License

This project is for educational and portfolio purposes.
