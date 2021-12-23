class DataSet:
    '''
    DataSet is an object that encapsulates a 2D square list of numbers and allow operations on them.
    '''

    # The internal data set is a 2D list of floats.
    def __init__(self, data_set):
        '''
        C'tor takes data_set as a 2D list, then it calculates the row/column count for future use.

        The data_set must not be None and must be a square 2D list, no jaggie lists allowed.
        '''

        # Store off the internal data set.
        self.data_set = data_set
        
        # Calculate the row and column count just once in the c'tor.

        # The row count is simply the length of the 'outer' list of rows.
        self.row_count = len(data_set)
        
        # Count the columns if we have a row, otherwise it's zero. Assumes we have a square 2D list.
        if(self.row_count > 0):
            # Get the length of the first column as we assume that we have a 2D data set.
            self.column_count = len(data_set[0])
        else:
            self.column_count = 0

    def get_row_count(self):
        '''
        Get the row count that we set in the c'tor.
        '''
        return self.row_count

    def get_column_count(self):
        '''
        Get the column count that we set in the c'tor.
        '''
        return self.column_count

    def __iter__(self):
        '''
        Let consumers iterate over this object as if it was the raw underlying 2D list.
        '''

        for data_cell in self.data_set:
              yield data_cell

    def __getitem__(self, row_column_tuple):
        '''
        Allow 2D list like access by using a tuple with the subscript method.
        '''
        row, column = row_column_tuple
        
        return self.data_set[row][column]

    def __eq__(self, other):
        '''
        Equality operator, great for comparing DataSet objects.
        '''
        if isinstance(other, self.__class__):
            return self.data_set == other.data_set
        else:
            return False

    def __ne__(self, other):
        '''
        inequality operator, just the opposite of the equality operator.
        '''
        return not self.__eq__(other)
        
    def __str__(self):
        '''
        Simply prints the data set to the screen in a nice square.
        '''

        row_chunks = []
        row_index = 0

        # Loop each row of the data set.
        for row in self.data_set:
            
            column_chunks = []
            column_index = 0
            
            # Loop each column of the current row.
            for column in row:

                # Print the column and add a space at the end.
                cell_data = str(self.data_set[row_index][column_index])
                
                # Add asterisks around any 'None' value to highlight it.
                if(cell_data == "None"):
                    column_chunks.append(f"**{cell_data}**")
                else:
                    column_chunks.append(cell_data)

                column_chunks.append(" ")
                column_index += 1

            # Add a new line at the end of the row.
            column_chunks.append("\n")

            # Join all the column chunks into one row string.
            row_chunks.append(''.join(column_chunks))

            row_index += 1

        # Return all the rows into one string.
        return ''.join(row_chunks)

    
