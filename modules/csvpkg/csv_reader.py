import csv

def LoadDataSetFromCsv(filename, delimiter):
    
    '''
    This function opens the csv file specified in 'filename' and reads it row by row.

    The cell data is converted from a string to a float where possible, or if a 'nan' value is encountered,
    converts it to None instead.
    '''

    # Open the file specified in function param 'filename'
    with open(filename, newline='') as csvfile:

        # The data list of rows (of columns) that we will return at the end of this function.
        data_rows = []

        # Create a CSV file reader with the opened CSV file.
        csvreader = csv.reader(csvfile, delimiter=delimiter)
        
        # Read one row of the CSV at a time.
        for row in csvreader:

            # Create one row list to put cell data into after type conversion.
            data_row = []

            # Iterate each cell of the current row.
            for cell in row:

                # Attempt to convert from a string to a float, unless we detect 'nan' then use None instead.
                if(cell == 'nan'):
                    cell_value = None
                else:
                    try:
                        cell_value = float(cell) # It should be a valid float, attempt to cast.
                    except ValueError:
                        cell_value = None # Could not cast to float, put None in that cell.

                # Append the value that was converted from a string to a value into the current row.
                data_row.append(cell_value)

            # Finished converting values in the current row, append it to the list of rows.
            data_rows.append(data_row)
    
    # Return all the converted cells as a 2D list.
    return data_rows

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