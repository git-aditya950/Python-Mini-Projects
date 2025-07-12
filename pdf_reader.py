import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import PyPDF2
from openai import OpenAI

client = OpenAI(api_key="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")  # replace with your OpenAI key

class PDFChatApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chat with PDF (Powered by GPT)")
        self.geometry("720x500")
        self.pdf_text = ""

        self.init_ui()

    def init_ui(self):
        self.upload_btn = ctk.CTkButton(self, text="📁 Upload PDF", command=self.load_pdf)
        self.upload_btn.pack(pady=10)

        self.input_field = ctk.CTkEntry(self, width=500, font=("Arial", 14))
        self.input_field.pack(pady=10)
        self.input_field.insert(0, "Ask something about the PDF...")

        self.ask_btn = ctk.CTkButton(self, text="Ask PDF ➤", command=self.ask_pdf)
        self.ask_btn.pack(pady=10)

        self.result_box = ctk.CTkTextbox(self, width=680, height=300, font=("Consolas", 13), wrap="word")
        self.result_box.pack(pady=10)

    def load_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if not file_path:
            return

        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                self.pdf_text = ""
                for page in reader.pages:
                    self.pdf_text += page.extract_text()
            self.result_box.insert(tk.END, "✅ PDF uploaded and processed successfully.\n\n")
        except Exception as e:
            self.result_box.insert(tk.END, f"❌ Failed to read PDF: {e}\n\n")

    def ask_pdf(self):
        question = self.input_field.get()
        if not self.pdf_text:
            self.result_box.insert(tk.END, "⚠️ Please upload a PDF first.\n")
            return
        if not question.strip():
            self.result_box.insert(tk.END, "⚠️ Please enter a question.\n")
            return

        self.result_box.insert(tk.END, f"🧠 You: {question}\n")

        try:
            prompt = f"You are reading the following PDF content:\n\n{self.pdf_text[:3000]}\n\nNow answer this: {question}"
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content.strip()
            self.result_box.insert(tk.END, f"🤖 GPT: {answer}\n\n")
        except Exception as e:
            self.result_box.insert(tk.END, f"❌ Error: {str(e)}\n")

if __name__ == "__main__":
    app = PDFChatApp()
    app.mainloop()
