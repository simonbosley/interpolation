import sys
from os.path import exists

sys.path.insert(0, "./modules")
# print(sys.path) # Uncomment this line if you're having trouble adding the local 'modules' directory to the python sys path, './modules' should come first

# Csv imports
from modules.csvpkg import FileNamesArgsReader
from modules.csvpkg import FileNames
from modules.csvpkg import LoadDataSetFromCsv
from modules.csvpkg import WriteDataSetToCsv

# Data imports
from modules.datapkg import DataSet
from modules.datapkg import DataSetTransformations

# Create our comand line argument reader to extract the input and output file names.
fileNames = FileNamesArgsReader.translate_args(sys.argv)

# Check if we were able to receive the file names
if(fileNames == None):
    print(f'Unable to read file names from the command line arguments, error:\n\t{FileNamesArgsReader.last_error}')
    quit()

if(fileNames.input_filename == fileNames.output_filename):
    print(f"input filename and output filename are the same, please specify different filename so you don't erase data")
    quit()

# Set the delimiter to use in CSV files.
delimiter = ','

# Load input file and create a DataSet from it.
input_data = LoadDataSetFromCsv(fileNames.input_filename, delimiter)
input_data_set = DataSet(input_data)

# Transform the DataSet by interpolating missing values, converting any values to 7 decimal places when interpolating.
transformed_data_set = DataSetTransformations.InterpolateMissingValues(input_data_set, dp_rounding=7)

# Write transformed DataSet to CSV file, using ',' as delimiter
WriteDataSetToCsv(transformed_data_set, fileNames.output_filename, delimiter)