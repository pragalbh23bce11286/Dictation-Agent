import os
import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
import PyPDF2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 


root = tk.Tk()
root.title("Dictation Agent")
root.geometry("500x400")


def read_text():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("start output.mp3")  # Works for Windows, use "afplay output.mp3" on macOS
    else:
        messagebox.showwarning("Warning", "No text to read!")


def read_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file_path:
        return
    
    try:
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = "\n".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
        
        if text:
            tts = gTTS(text=text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3")
        else:
            messagebox.showwarning("Warning", "No text extracted from the PDF!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read PDF: {e}")


def read_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    try:
        text = pytesseract.image_to_string(Image.open(file_path))
        if text:
            tts = gTTS(text=text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3")
        else:
            messagebox.showwarning("Warning", "No text found in the image!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process image: {e}")


tk.Label(root, text="Enter Text to Dictate:", font=("Arial", 12)).pack(pady=5)
text_box = tk.Text(root, height=5, width=50)
text_box.pack()

tk.Button(root, text= " Read Text", command=read_text).pack(pady=5)
tk.Button(root, text= " Read from PDF", command=read_pdf).pack(pady=5)
tk.Button(root, text= " Read from Image", command=read_image).pack(pady=5)

root.mainloop()
