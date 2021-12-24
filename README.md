# interpolation
This is a python project and requires python3 to be installed to run the test scripts.

This project let's you:

    1. Read a CSV file of values into a 2D list.
    2. Create a DataSet object from a 2D list.
    3. Tranform a DataSet object.
    4. Write a CSV file from a DataSet object.

The currently available transformation 'InterpolateMissingValues' (in file modules/datapkg/data_set_transformations) allows you to 
convert any missing values in an input DataSet and replace them with an interpolated value in the output DataSet (other values are left as is).
Missing values are interpolated by averaging all the available non-diagonal values adjacent to the missing value.

The main re-usable functionality of the project is placed in packages in the modules folder. 
To use them in your own python scripts you can read the 'run_unit_tests.py' to see how this is done.

# requirements

You will need to run this project on a unix based system with python3 installed.

# getting started

Simply clone the repo to a local directory on your system, and navigate to the 'interpolation' root directory.

# acceptance tests
To run the acceptance tests run the following shell script:

```console
./acceptance_shell.sh
```

If you don't have permissions to execute, do a chmod +x on the file.

# unit tests
To run the unit tests navigate to the root interpolation folder, then run the following command:

```console
python3 run_unit_tests.py
```

# using the python file yourself

To transform an input CSV file to a specified output CSV file, then run the command as follows:

```console
python3 interpolate_data.py example_data/input_test_data.csv example_data/transformed_input_test_data_set.csv"
```
