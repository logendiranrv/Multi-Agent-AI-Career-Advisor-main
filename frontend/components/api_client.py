import os
import requests

API_BASE = os.getenv("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")
TIMEOUT_SECONDS = 120


def _api_url(path: str) -> str:
    return f"{API_BASE}{path}"


def check_health() -> bool:
    """Return True if the backend API is reachable."""
    try:
        # Increased timeout to 30s to handle Render free tier cold starts
        resp = requests.get(_api_url("/health"), timeout=30)
        return resp.status_code == 200
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False


def analyze_resume(file):
    """
    Send a resume file to the backend for analysis.

    Raises a descriptive exception on failure.
    """
    try:
        response = requests.post(
            _api_url("/analyze"),
            files={"file": (file.name, file, file.type or "application/octet-stream")},
            timeout=TIMEOUT_SECONDS,
        )
    except requests.ConnectionError:
        raise ConnectionError(
            "Unable to reach the backend server. "
            "Ensure it is running at " + API_BASE
        )
    except requests.Timeout:
        raise TimeoutError(
            "The analysis request timed out. "
            "The resume may be too large or the server is under heavy load."
        )

    if response.status_code == 200:
        return response.json()

    # Surface the server error message when available
    try:
        detail = response.json().get("detail", response.text)
    except ValueError:
        detail = response.text

    raise RuntimeError(
        f"Analysis failed (HTTP {response.status_code}): {detail}"
    )