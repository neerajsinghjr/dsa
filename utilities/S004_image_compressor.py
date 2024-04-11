'''
-------------------------------------------------------------------------------------
-> Title: Image Compressor
-> Author: @neeraj-singh-jr
-> Created: 2024-04-09
-> Description:
-------------------------------------------------------------------------------------

Objective: Compress the image size

Run-Time Environment:-
1) Need a csv file with two columns
    - source_image_location :
        eg,
            /path/to/file (include filename)
            /Downloads/image/img_001.jpg

    - destination image_location : eg, /path/to/file (exclude filename)
            /Downloads/path

    - reduce_ratio (optional)
        eg, 75 - integer value only

    - max size in kb (optional)
        eg, 1024 kb is equals to 1 mb

-------------------------------------------------------------------------------------
'''
from csv import DictReader,DictWriter, reader, writer
from distutils.util import strtobool
from datetime import datetime
from time import time
from PIL import Image
import traceback
import sys
import os


# SCRIPT RUN TIME CONSTANTS;;
DEBUG = False
TASK = 'IMAGE_COMPRESSOR_SCRIPT'
LOG_FILE = 'S000_runtime_log.log'
LOG_FORMAT = "[##time##][##type##::##task##] :: ##message## \n"


# SCRIPT CONSTANTS ONLY;;
REDUCE_RATIO = 90
DEFAULT_DIR = '/tmp/'
MAX_SIZE_KB= 1800

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


def generate_file_name(filename=None):
    suffix = round(time())
    if not filename:
        filename = 'Image_Converted_{suffix}.jpg'
        return filename

    file, ext = filename.split('.')
    file = file.replace(' ', '_')
    filename = file + f'_{time()}.' + ext

    return filename


def runner(params):
    # Create you main script logic here;;
    def reduce_image_size(input_image_path, output_image_path, max_size_kb):
        """
        Reduces the size of the image located at input_image_path
        and saves the resized image to output_image_path with a target maximum size in KB.
        """
        # Soruce image name;;
        source_img_name = params['source_image']

        # Open the input image
        image = Image.open(source_img_name)

        # Get the original image size in bytes
        original_size_kb = os.path.getsize(source_img_name) / 1024

        # Calculate the target quality based on the desired max size
        target_quality = params['reduce_ratio']

        # Output directory generation;;
        output_dir = params.get('target_folder')
        if '/' == output_dir[-1]:
            output_dir += '/'

        base_filename = None
        if '/' in source_img_name:
            base_filename = source_img_name.split('/')[-1]

        output_image = output_dir + generate_file_name(base_filename)

        while True:
            # Save the image with the current quality
            image.save(output_image, quality=target_quality)

            # Get the size of the saved image in KB
            saved_size_kb = os.path.getsize(output_image_path) / 1024

            # Check if the saved size is within the target max size
            if saved_size_kb <= max_size_kb:
                break

            # If the saved size is still too large, reduce the quality further
            target_quality -= 5
            if target_quality <= 0:
                raise ValueError("Unable to reduce image size to the specifiedßß limit")

        # TODO: Store the record in the csv for better readable usages;;

        lognow(f"Image Convered Successfully, Source image: {params['source_image']}, target: target_image")

        return target_quality, original_size_kb, saved_size_kb


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
    # Script Main Variable;;
    file = options[-1]
    with open(file, 'r') as rf:
        params = {}
        reader = DictReader(rf)
        for row in reader:
            params['source_image'] = row['source_image']
            params['target_folder'] = row.get('target_folder') or DEFAULT_DIR
            params['max_size_kb'] = row.get('max_size_kb') or MAX_SIZE_KB
            params['reduce_ratio'] = row.get('reduce_ratio') or REDUCE_RATIO
            lognow(f'Starting file converstion with constraints : {params}')
            try:
                # Script with exit code;;
                exit_code = runner(params)
                if exit_code:
                    lognow(f"Task: {TASK} Completed Successfully")
                else:
                    lognow(f"Task: {TASK} Ter Failed  Successfully")
            except Exception as ex:
                lognow(f"Error Traced in Script : {traceback.format_exc()}", type='ex')

    lognow("Script Reached End ...")