# The files we're using.
INPUT_FILNAME="example_data/input_test_data.csv"
OUTPUT_FILENAME="example_data/transformed_input_test_data_set.csv"
EXPECTED_OUTPUT_FILENAME="example_data/interpolated_test_data.csv"

# The commands we're going to run.
TRANSFORM_COMMAND="python3 interpolate_data.py $INPUT_FILNAME $OUTPUT_FILENAME"
DIFF_COMMAND="diff $OUTPUT_FILENAME $EXPECTED_OUTPUT_FILENAME"

# Run the transform command
echo
echo "Running transform command: '$TRANSFORM_COMMAND'"
$TRANSFORM_COMMAND

# Test the output matches the expected output by using the diff command.
echo
echo "Testing output file with the diff command: '$DIFF_COMMAND'"
$DIFF_COMMAND

# Take the return code of the diff command, 0=SUCCESS, anything else is FAILURE.

echo
echo "Return code: $?."
echo

if [ $? == 0 ]
then
   echo "The output file and expected output file are identical, test SUCCESS."
else
   echo "The output file and expected output file are NOT identical, test FAILURE."
fi

echo