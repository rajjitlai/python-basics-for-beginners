# Project 03 - PDF Reader

import pyttsx3
import PyPDF2


def read_pdf(file_path):
    engine = pyttsx3.init()

    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()

            if text:
                print(f"Reading page {page_num + 1}...")
                engine.say(text)
                engine.runAndWait()


if __name__ == "__main__":
    pdf_path = input("Enter the PDF file path: ")
    read_pdf(pdf_path)
