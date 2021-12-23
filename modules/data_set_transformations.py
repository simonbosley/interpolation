from modules import DataSet

class DataSetTransformations:
    '''
    This class acts as th set of transformations that can be applied to a DataSet
    '''

    @classmethod
    def InterpolateMissingValues(cls, dataSet):
        '''
        Take the passed data_set and create a new data_set with interpolated missing values.
        '''

        transformed_data_set = [[0.0 for column in range(dataSet.get_column_count())] for row in range(dataSet.get_row_count())]

        # Loop each row of the data set.

        row_index = 0

        for row in dataSet:

            column_index = 0

            # Loop each column of the current row.
            for cell in row:

                # Do we need to interpolate?
                if(cell == None):
                    
                    interpolated_value = 0.0
                    total_of_values_to_interpolate = 0
                    count_of_values_to_interpolate = 0

                    # Try to get the value above.
                    if(row_index - 1 >= 0):
                        total_of_values_to_interpolate += dataSet[row_index - 1, column_index]
                        count_of_values_to_interpolate += 1 

                    # Try to get the value to the left.
                    if(column_index -1 >= 0):
                        total_of_values_to_interpolate += dataSet[row_index, column_index - 1]
                        count_of_values_to_interpolate += 1

                    # Try to get the value below.
                    if(row_index + 1 <= dataSet.get_row_count() - 1):
                        total_of_values_to_interpolate += dataSet[row_index + 1, column_index]
                        count_of_values_to_interpolate += 1
                    
                    # Try to get the value to the right.
                    if(column_index + 1 <= dataSet.get_column_count() - 1):
                        total_of_values_to_interpolate += dataSet[row_index, column_index + 1]
                        count_of_values_to_interpolate += 1

                    # Avoid the divide by 0 error.
                    if(count_of_values_to_interpolate > 0):
                        interpolated_value = round(total_of_values_to_interpolate / count_of_values_to_interpolate, 7)

                    transformed_data_set[row_index][column_index] = interpolated_value
                else:
                    transformed_data_set[row_index][column_index] = cell

                column_index += 1
            
            row_index += 1

        return DataSet(transformed_data_set)