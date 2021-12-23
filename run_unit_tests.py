import sys

sys.path.insert(0, "./modules")

#print(sys.path) # Uncomment this line if you're having trouble adding 'modules' to the python sys path, './modules' should come first, to avoid clashing with any other local module package.

from modules import DataSet
from modules import DataSetTransformations

def test_row_count(data_set, expected_row_count):
    '''
    Test the DataSet get_row_count function.
    '''
    return data_set.get_row_count() == expected_row_count

def test_column_count(data_set, expected_column_count):
    '''
    Test the DataSet get_column_count function.
    '''
    return data_set.get_column_count() == expected_column_count

def compare_data_set_sizes(data_set1, data_set2):
    '''
    Compare the row and column count of two data sets.
    '''

    return data_set1.get_row_count() == data_set2.get_row_count() and \
        data_set1.get_column_count() == data_set2.get_row_count()

# Create a test data set.
test_data_2d_array = \
[[37.454012,95.071431,73.199394,59.865848,None],
[15.599452,5.808361,86.617615,60.111501,70.807258],
[2.058449,96.990985,None,21.233911,18.182497],
[None,30.424224,52.475643,43.194502,29.122914],
[61.185289,13.949386,29.214465,None,45.606998]]

test_data_set = DataSet(test_data_2d_array)

print("\nUsing DataSet:\n")
print(str(test_data_set))
print()

expected_row_count = 5
expected_column_count = 5

if(test_row_count(test_data_set, expected_row_count)):
    print(f"test_data_set.get_row_count() returned expected_row_count {expected_row_count}. PASS")
else:
    print(f"test_data_set.get_row_count() returned {test_data_set.get_row_count()}, expected_row_count was {expected_row_count}. FAIL")

if(test_column_count(test_data_set, expected_column_count)):
    print(f"test_data_set.get_column_count() returned expected_column_count {expected_column_count}. PASS")
else:
    print(f"test_data_set.get_column_count() returned {test_data_set.get_column_count()}, expected_column_count was {expected_column_count}. FAIL")


# Now try transforming the test data set.
transformed_test_data_set = DataSetTransformations.InterpolateMissingValues(test_data_set)

# The transformed data set returned must not be None.
if(transformed_test_data_set == None):
    print("DataSetTransformations.InterpolateMissingValues(test_data_set) returned 'None'. FAIL")
    quit()

# The transformed data set should have the same column size and row size as its input data set.
if not compare_data_set_sizes(test_data_set, transformed_test_data_set):
    print("test_data_set not the same size as transformed_test_data_set. FAIL")
    quit()

# Create the expected transformed data set, that should match the test data set after transformation.
expected_test_data_2d_array_transformed = \
[[37.454012,95.071431,73.199394,59.865848,65.336553],
[15.599452,5.808361,86.617615,60.111501,70.807258],
[2.058449,96.990985,64.3295385,21.233911,18.182497],
[31.222654,30.424224,52.475643,43.194502,29.122914],
[61.185289,13.949386,29.214465,39.338655,45.606998]]

expected_transformed_dataset = DataSet(expected_test_data_2d_array_transformed)

print("\nExpected transformed DataSet:\n")
print(str(expected_transformed_dataset))

print("\nActual transformed DataSet:\n")
print(str(transformed_test_data_set))

if(transformed_test_data_set == expected_transformed_dataset):
    print("transformed_test_data_set was the same as the expected_transformed_dataset. SUCCESS.")
else:
    print("transformed_test_data_set was not the same as the expected_transformed_dataset. FAIL.")


print(expected_test_data_2d_array_transformed)