'''
-------------------------------------------------------------------------------------
-> Title: PDF to Docx Convertor
-> Author: @neeraj-singh-jr
-> Created: 2024-04-20
-> Description:
-------------------------------------------------------------------------------------

Convert PDF file to Docx

-------------------------------------------------------------------------------------
'''
from csv import DictReader,DictWriter, reader, writer
from distutils.util import strtobool
from datetime import datetime
from docx import Document
from time import time
import pdfplumber
import traceback
import sys
import os


# SCRIPT RUN TIME CONSTANTS;;
DEBUG = False
TASK = 'PDF DOCX CONVERTOR'
LOG_FILE = 'script_logs.log'
LOG_FORMAT = "[##time##][##type##::##task##] :: ##message## \n"


def lognow(message, type='info'):
    line = LOG_FORMAT
    time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    type = 'INFO' if type == 'info' else 'ERROR'
    with open(LOG_FILE, 'a') as file_obj:
        line = line.replace("##time##", time)
        line = line.replace("##task##", TASK)
        line = line.replace("##type##", type)
        line = line.replace("##message##", message)
        file_obj.write(line)
        if DEBUG: print(line)


def runner(params):
    # Create you main script logic here;;
    pdf_path = params.get('pdf_path')
    docx_path = params.get('docx_path')
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Create a new Word document
        doc = Document()

        # Iterate through each page of the PDF
        for page in pdf.pages:
            # Extract text from the page
            text = page.extract_text()

            # Add the text to the Word document
            doc.add_paragraph(text)

        # Save the Word document
        doc.save(docx_path)

    return True

# Specify the paths for the PDF and DOCX files
if __name__ == "__main__":
    params = {}
    options = sys.argv
    opt_len = len(options)
    if ('-d' in options or '--debug' in options) and opt_len == 4:
        DEBUG = strtobool(options[-2])
    else:
        if len(options) < 2:
            print("Task Abort::Requirements Unsatisfied")
            sys.exit(1)
    lognow(f"DEBUG Mode: {DEBUG}")

    # Script Main Variable;;
    params['pdf_path'] = options[-2]
    params['docx_path'] = options[-1]

    try:
        # Script with exit code;;
        exit_code = runner(params)
        if exit_code:
            lognow(f"Task: {TASK} Completed Successfully")
        else:
            lognow(f"Task: {TASK} Completed Successfully")

    except Exception as ex:
        lognow(f"Error Traced in Script : {traceback.format_exc()}", type='ex')

    lognow("Script Reached End ...")