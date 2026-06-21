from pypdf import PdfReader
from docx import Document
import os

class DocumentAgent:

    def extract_text(self, file_path):

        ext = os.path.splitext(file_path)[1].lower()

        if ext == ".pdf":
            return self._read_pdf(file_path)

        elif ext == ".docx":
            return self._read_docx(file_path)

        else:
            raise ValueError("Unsupported file type")

    def _read_pdf(self, file_path):

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text

    def _read_docx(self, file_path):

        doc = Document(file_path)

        text = "\n".join([para.text for para in doc.paragraphs])

        return text