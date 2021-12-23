import csv

def LoadDataSetFromCsv(filename):

    with open(filename, newline='') as csvfile:

        data = []
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        
        # Read one row of the CSV at a time.
        for row in csvreader:

            # Create a row list to put cell data into after type conversion.
            data_row = []

            # Iterate each cell of the current row.
            for cell in row:

                # Read the value as a float.
                if(cell == 'nan'):
                    cell_value = None
                else:
                    try:
                        cell_value = float(cell)
                    except ValueError:
                        cell_value = None

                data_row.append(cell_value)

            data.append(data_row)
    
    return data

'''
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
'''