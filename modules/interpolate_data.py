import sys

from modules import FileNamesArgsReader

# Create our comand line argument reader to extract the input and output file names.
fileNames = FileNamesArgsReader.translate_args(sys.argv)

# Check if we were able to receive the file names
if(fileNames == None):
    print(f'Unable to read file names from the command line arguments, error:\n\t{FileNamesArgsReader.last_error}')
    quit()

if(fileNames.input_filename == fileNames.output_filename):
    print(f"input filename and output filename are the same, please specify different filename so you don't erase data")
    quit()

# Print the file names here
print(f"Received command line arg filenames: input filename '{fileNames.input_filename}' and output filename '{fileNames.output_filename}'")