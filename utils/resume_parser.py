import pdfplumber
import pytesseract
from docx import Document
from PIL import Image
from pdf2image import convert_from_bytes
import io
import os

# 🔧 Set tesseract path (CHANGE if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except:
        pass
    return text.strip()


def extract_text_from_scanned_pdf(file):
    text = ""
    try:
        images = convert_from_bytes(file.read())
        for img in images:
            text += pytesseract.image_to_string(img)
    except:
        pass
    return text.strip()


def extract_text_from_docx(file):
    try:
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs).strip()
    except:
        return ""


def extract_text_from_image(file):
    try:
        image = Image.open(file)
        return pytesseract.image_to_string(image).strip()
    except:
        return ""


def extract_text_from_txt(file):
    try:
        return file.read().decode("utf-8").strip()
    except:
        return ""


def extract_resume_text(file):
    filename = file.filename.lower()

    # 1️⃣ PDF
    if filename.endswith(".pdf"):
        file_bytes = file.read()
        file.seek(0)

        text = extract_text_from_pdf(file)
        if text:
            return text

        # fallback to OCR
        return extract_text_from_scanned_pdf(io.BytesIO(file_bytes))

    # 2️⃣ DOC / DOCX
    elif filename.endswith(".docx") or filename.endswith(".doc"):
        return extract_text_from_docx(file)

    # 3️⃣ TXT
    elif filename.endswith(".txt"):
        return extract_text_from_txt(file)

    # 4️⃣ IMAGE
    elif filename.endswith((".png", ".jpg", ".jpeg")):
        return extract_text_from_image(file)

    else:
        return ""
