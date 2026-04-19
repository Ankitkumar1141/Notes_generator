from PyPDF2 import PdfReader


def extract_text(file) -> str:
    reader = PdfReader(file)
    text_parts = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_parts.append(page_text)

    return "\n".join(text_parts).strip()
