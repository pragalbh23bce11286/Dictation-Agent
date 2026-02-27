# Dictation Agent
Text-to-Speech Desktop Application with PDF & Image OCR Support

Dictation Agent is a desktop application built using Tkinter that converts:

1. Typed text

2. PDF documents

3. Images containing text

into spoken audio using Text-to-Speech (TTS) technology.

This tool combines OCR and speech synthesis to create an accessible reading assistant.

# Features

1. Convert typed text to speech

2. Extract and read text from PDF files

3. Extract text from images using OCR

4. Generate MP3 output automatically

5. Simple and user-friendly GUI

# Technologies Used
Technology	Purpose
Tkinter	GUI Interface
gTTS	Text-to-Speech
PyPDF2	PDF Text Extraction
pytesseract	OCR for images
Tesseract OCR	OCR Engine
Pillow	Image Processing

# System Architecture
User Input
   │
   ├── Typed Text → gTTS → MP3 → Audio Playback
   │
   ├── PDF File → PyPDF2 → Extract Text → gTTS → MP3 → Audio
   │
   └── Image File → Tesseract OCR → Extract Text → gTTS → MP3 → Audio
   
# Application Workflow
1. Text-to-Speech from Input Box

User types text

gTTS converts text to speech

Audio saved as output.mp3

Automatically played

2. Read from PDF

User selects a PDF file

Text extracted using PyPDF2

Converted to speech

Audio played automatically

3️. Read from Image (OCR)

User selects an image

OCR performed using Tesseract

Extracted text converted to speech

Audio played

# Installation Guide
Step 1: Clone Repository
git clone https://github.com/yourusername/dictation-agent.git
cd dictation-agent
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Install Tesseract OCR

Download and install:

Tesseract OCR

After installation, update the path in your code:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

For:

Windows → Use full installation path

macOS → Install via Homebrew (brew install tesseract)

Linux → Install via apt (sudo apt install tesseract-ocr)

# Requirements
gTTS
PyPDF2
pytesseract
Pillow

(Tkinter comes pre-installed with most Python distributions.)

# How to Run
python dictation_agent.py

The GUI window will open with:

Text input box

"Read Text" button

"Read from PDF" button

"Read from Image" button

# Use Cases

Accessibility tool for visually impaired users

Study assistant (listen to PDFs)

Language learning aid

Reading scanned documents aloud

Productivity tool for multitasking
