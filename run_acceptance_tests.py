import sys

sys.path.insert(0, "./modules")
# print(sys.path) # Uncomment this line if you're having trouble adding the local 'modules' directory to the python sys path, './modules' should come first

from modules.csvpkg import LoadDataSetFromCsv
from modules.datapkg import DataSet
from modules.datapkg import DataSetTransformations

print("\nRunning acceptance tests...\n")

# Set the delimiter we expect in CSV files.
delimiter = ','

# Use our handy csv library to load the csv file into a 2D list.
input_test_data = LoadDataSetFromCsv("./example_data/input_test_data.csv", delimiter)

# Create a DataSet object from the 2D list.
input_test_data_set = DataSet(input_test_data)

# Print what we loaded.
print("Loaded input test data: \n\n" + str(input_test_data_set))

# Load the interpolated csv file.
interpolated_test_data = LoadDataSetFromCsv("./example_data/interpolated_test_data.csv", delimiter)

# Create a DataSet object from the 2D list.
interpolated_test_data_set = DataSet(interpolated_test_data)

# Print what we loaded.
print("Loaded interpolated test data: \n\n" + str(interpolated_test_data_set))

# Transform the input data set, set the decimal place precision to 7. 
transformed_input_test_data_set = DataSetTransformations.InterpolateMissingValues(input_test_data_set, dp_rounding=7)

# Print what we transformed.
print("Transformed input test data: \n\n" + str(transformed_input_test_data_set))

# Compare the original input test DataSet with the expected loaded interpolated DataSet, this should NOT match.
if not (input_test_data_set == interpolated_test_data_set):
    print("The input_test_data_set does not match the interpolated_test_data_set, as expected. SUCCESS.")
else:
    print("The input_test_data_set does match the interpolated_test_data_set, not expected. FAIL.")

# Compare the transformed input DataSet with the expected loaded interpolated DataSet.
if(transformed_input_test_data_set == interpolated_test_data_set):
    print("The transformed_input_test_data_set does match the expected interpolated_test_data_set. SUCCESS.")
else:
    print("The transformed_input_test_data_set does not match the expected interpolated_test_data_set. FAIL.")
