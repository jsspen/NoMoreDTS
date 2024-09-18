import os
import subprocess
import csv

# create directory if it doesn't exist
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    else:
        print(f"Directory already exists: {path}")

# run the ffmpeg command
def run_ffmpeg(INPUT_PATH, FULL_OUTPUT, FFMPEG_COMMAND):
    command = [
        "ffmpeg",
        "-i", INPUT_PATH,
        *FFMPEG_COMMAND.split(),
        FULL_OUTPUT
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Conversion successful! File saved at: {FULL_OUTPUT}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

# take user input rather than csv file
def manual_input():
    # Manual input mode
    USE_DEFAULT_PATHS = input('Do you want to use the default base paths? (y/n) ')

    if USE_DEFAULT_PATHS == 'y':
        # set by default
        INPUT_BASE = '/mnt/Beta14/Films/Temp/'
        OUTPUT_BASE = '/mnt/Beta14/Films/Features/'
        # file specific input
        OUTPUT_DIRECTORY = input(f'Destination path: {OUTPUT_BASE}')
        INPUT_FILE_PATH = input(f'Current path (including extension): {INPUT_BASE}')
        OUTPUT_FILENAME = input('Output filename? ')
        # combining default & input
        # output base + output directory = path for creating output directory if it doesn't exist
        OUTPUT_PATH = f"{OUTPUT_BASE}{OUTPUT_DIRECTORY}"
        # input base + input path = ffmpeg input
        INPUT_PATH = f"{INPUT_BASE}{INPUT_FILE_PATH}"
        # output path + output filename = ffmpeg output
        FULL_OUTPUT = f"{OUTPUT_PATH}/{OUTPUT_FILENAME}"
        # check
        print(f'Creating: {OUTPUT_PATH}')
        print(f'Processing: {INPUT_PATH}')
        print(f'Outputting: {FULL_OUTPUT}')
        ####### TO DO #######
        # correct = input('Is this correct?')
    else:
        OUTPUT_PATH = input('Enter the full path for the final destination directory: ')
        INPUT_PATH = input('Enter the full path for the current file, including extension: ')
        OUTPUT_FILENAME = input('What is the desired final filename? ')
        FULL_OUTPUT = f"{OUTPUT_PATH}/{OUTPUT_FILENAME}"
        print(f'Creating: {OUTPUT_PATH}')
        print(f'Processing: {INPUT_PATH}')
        print(f'Outputting: {FULL_OUTPUT}')
        ####### TO DO #######
        # correct = input('Is this correct?')

    # Give option to change command or use default
    FFMPEG_COMMAND = set_FFMPEG_COMMAND()
    # FFMPEG doesn't like if the output directory doesn't exist yet
    create_directory(OUTPUT_PATH)
    # Run the ffmpeg conversion
    run_ffmpeg(INPUT_PATH, FULL_OUTPUT, FFMPEG_COMMAND)

# Take a csv file as input
# currently accepts header row with
# OUTPUT_DIRECTORY, INPUT_FILE_PATH, OUTPUT_FILENAME
def csv_input():
    CSV_FILE = input('Enter the name of the CSV file: ')
    # Get command outside of the loop so you don't have to keep answering
    # Assumes you're going to use the same command for batch processing
    FFMPEG_COMMAND = set_FFMPEG_COMMAND()
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            # Skip first (header) row
            next(reader, None)
            for row in reader:
                OUTPUT_DIRECTORY, INPUT_FILE_PATH, OUTPUT_FILENAME = row
                # Currently using a default base path
                OUTPUT_PATH = f"/mnt/Beta14/Films/Features/{OUTPUT_DIRECTORY}"
                INPUT_PATH = f"/mnt/Beta14/Films/Temp/{INPUT_FILE_PATH}"
                FULL_OUTPUT = f"{OUTPUT_PATH}/{OUTPUT_FILENAME}"

                # Create destination directory
                create_directory(OUTPUT_PATH)
                # Run the ffmpeg conversion
                run_ffmpeg(INPUT_PATH, FULL_OUTPUT, FFMPEG_COMMAND)
    
    except FileNotFoundError:
        print(f"Error: CSV file '{CSV_FILE}' not found.")

def set_FFMPEG_COMMAND():
    FFMPEG_COMMAND = "-map 0 -c:v copy -c:a ac3 -b:a 640k -c:s copy"
    USE_DEFAULT_COMMAND = input(f'Do you want to use the default command: {FFMPEG_COMMAND}? (y/n) ')
    if USE_DEFAULT_COMMAND != 'y':
        FFMPEG_COMMAND = input('Enter the desired command: ')
    return FFMPEG_COMMAND
    
# Select input type
# csv file must be in root directory
INPUT_TYPE = input(f'Enter \'c\' for csv input or \'m\' for manual: ')
if INPUT_TYPE == 'c':
    csv_input()
if INPUT_TYPE == 'm':
    manual_input()
