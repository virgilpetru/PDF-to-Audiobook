#type in terminal to install the modules:
# pip install pyttsx3
# pip install PyPDF2
# pip install py3-tts


import pyttsx3
import PyPDF2

# Select PFD that you want to read
PDF = open("file.pdf", "rb")

# Create PDF filereader
read_pdf = PyPDF2.PdfReader(PDF)

# Select the page you want to read
page = read_pdf.pages[0]

# Select text from the page
text = page.extract_text()

# Read the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()