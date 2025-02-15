import pyttsx3
import PyPDF2
import customtkinter as ctk
from threading import Thread


class PDFReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Chaoba's PDF Reader")
        self.root.geometry("500X300")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.label = ctk.CTkLabel(root, text="Select a PDF file: ")
        self.label.pack(pady=10)
        self.entry = ctk.CTkEntry(root, width=250)
        self.entry.pack(pady=10)
        self.browse_button = ctk.CTkButton(root, text="Browse", command=self.browse_pdf)
        self.browse_button.pack(pady=10)
        self.start_button = ctk.CTkButton(root, text="Start Reading", command=self.start_read)
        self.start_button.pack(pady=10)
        self.stop_button = ctk.CTkButton(root, text="Stop", command=self.stop_read)
        self.stop_button.pack(pady=10)

        self.status = ctk.CTkLabel(root, text="Status: Idle")
        self.status.pack(pady=10)

        self.engine = pyttsx3.init()
        self.reading = False
        self.current_page = 0
        self.total_pages = 0

    def browse_pdf(self):
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        self.entry.delete(0, "end")
        self.entry.insert(0, file_path)

    def start_read(self):
        file_path = self.entry.get()
        if file_path:
            self.reading = True
            thread = Thread(target=self.read_pdf, args=(file_path,))
            thread.start()

    def stop_read(self):
        self.reading = False
        self.engine.stop()
        self.status.configure(text="Status: Stopped")

    def read_pdf(self, file_path):
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            self.total_pages = len(reader.pages)

            for self.current_page in range(self.total_pages):
                if not self.reading:
                    break
                text = reader.pages[self.current_page].extract_text()

                if text:
                    self.status.configure(text=f"Reading page number {self.current_page + 1} of {self.total_pages}...")
                    self.engine.say(text)
                    self.engine.runAndWait()

        self.status.configure(text="Status: Finished")


if __name__ == "__main__":
    root = ctk.CTk()
    app = PDFReader(root)
    root.mainloop()

# Resume reading
# Specific page reading start
