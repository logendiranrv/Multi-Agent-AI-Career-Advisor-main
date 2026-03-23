import pdfplumber
import docx


def parse_pdf(file_path: str) -> str:
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def parse_docx(file_path: str) -> str:
    doc = docx.Document(file_path)

    text = "\n".join([para.text for para in doc.paragraphs])

    return text


def extract_resume_text(file_path: str) -> str:
    """
    Detect file type and extract text.
    """

    if file_path.endswith(".pdf"):
        return parse_pdf(file_path)

    elif file_path.endswith(".docx"):
        return parse_docx(file_path)

    else:
        raise ValueError("Unsupported file format")