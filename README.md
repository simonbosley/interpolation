# interpolation
This is a python project and requires python3 to be installed to run the test scripts.

This project let's you:

    1. Read a CSV file of values into a 2D list
    2. Create a DataSet object from a 2D list.
    3. Tranform a DataSet object.
    4. Write a CSV file from a DataSet.

The currently available transformation allows you to convert any missing values in an input DataSet
and replace them with an interpolated value in the output DataSet (other values are left as is).
Missing values are interpolated by averaging all the available non-diagonal values adjacent to the missing value.

The main re-usable functionality of the project is placed in packages in the modules folder. 
To use them in your own python scripts you can read the 'run_acceptance_tests.py' and 'run_unit_tests.py' to see how this is done.

To get started, clone the repo, and navigate to the 'interpolation' root directory. See below for how to run the test scripts.

# unit tests
To run the unit tests navigate to the root interpolation folder, then run the following command:

python3 run_unit_tests.py

# acceptance tests
To run the acceptance tests navigate to the root interpolation folder, then run the following command:

python3 run_acceptance_tests.py