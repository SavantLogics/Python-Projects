# Description: This program convert a PDF file to an audio book

# Import libraries
import pyttsx3
import pdfplumber
import PyPDF2


# Get the file name and location of the PDF file
file = 'Hawkins_Skill_Based_Resume.docx.pdf'

# Create a PDF File Object
pdfFileObj = open(file, 'rb')

# Create a PDF File Reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Get the number of pages
pages = pdfReader.numPages

# Create a pdfplumber object and loop through the number of pages in PDF file
with pdfplumber.open(file) as pdf:
    # Loop through the number of pages
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
