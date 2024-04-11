from distutils.util import strtobool
from datetime import datetime
import PyPDF2
import sys

# Script Variable;;
DEBUG = False
TASK = 'PDF Merge Script'
LOG_FILE = 'S000_py_runtime.log'
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

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    # Open the PDFs
    with open(pdf1_path, 'rb') as pdf1, open(pdf2_path, 'rb') as pdf2:
        # Create PDF reader objects
        pdf_reader1 = PyPDF2.PdfReader(pdf1)
        pdf_reader2 = PyPDF2.PdfReader(pdf2)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Append pages from the first PDF
        for page_num in range(len(pdf_reader1.pages)):
            pdf_writer.add_page(pdf_reader1.pages[page_num])

        # Append pages from the second PDF
        for page_num in range(len(pdf_reader2.pages)):
            pdf_writer.add_page(pdf_reader2.pages[page_num])

        # Write the merged PDF to the output file
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

# Example usage
pdf1_path = 'path/to/first.pdf'
pdf2_path = 'path/to/second.pdf'
output_path = 'path/to/merged.pdf'

merge_pdfs(pdf1_path, pdf2_path, output_path)

if __name__ == "__main__":
    options = sys.argv
    opt_len = len(options)
    if ('-d' in options or '--debug' in options) and opt_len == 4:
        DEBUG = strtobool(options[-2])
    else:
        if len(options) < 2:
            print("Task Abort::Requirements Unsatisfied")
            sys.exit(1)
    lognow(f"DEBUG Mode: {DEBUG}")
    params = {
        'inv': apps.get_model('core_services', 'Investments'),
        'txn': apps.get_model('core_services', 'Transactions'),
        'lb_callback': apps.get_model('core_services', 'LendboxCallbacks'),
        'wallet': apps.get_model('lendbox', 'LendboxWalletOrder'),
        'userprofile': apps.get_model('userprofile', 'UserProfile')
    }
    file = options[-1]
    with open(file, 'r') as rf:
        reader = DictReader(rf)
        for row in reader:
            try:
                pid = row['partner_ref_id']
                exit_load = row['exit_load']
                # for type :- pre_mature refund or 10L+ Limit refund ;;
                is_premature = strtobool(row.get('is_premature', True))
                # is_sms_enabled : default not delievered;;
                is_sms_enabled = strtobool(row.get('is_sms_enabled', False))
                if pid and exit_load:
                    lognow(f"Processing PartnerId: {pid}")
                    params['pid'] = pid
                    params['exit_load'] = exit_load
                    params['is_premature'] = is_premature
                    params['is_sms_enabled'] = is_sms_enabled
                    generate_debit_order(params)
                lognow("Task Completed")

            except Exception as ex:
                lognow(f"Error Occured : {traceback.format_exc()}", type='ex')
                print(f"Error: ", traceback.format_exc())