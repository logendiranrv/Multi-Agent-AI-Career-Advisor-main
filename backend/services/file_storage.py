import os
from fastapi import UploadFile
from core.settings import settings


def save_uploaded_file(file: UploadFile) -> str:
    """
    Save uploaded resume file and return file path.
    """

    os.makedirs(settings.RESUME_UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(settings.RESUME_UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path