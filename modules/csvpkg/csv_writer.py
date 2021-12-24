import csv

def WriteDataSetToCsv(data_set, filename, delimiter):
    '''
    Takes the input DataSet object in data_set and writes it to a CSV file with 
    the specified filename and delimiter.
    '''

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter, lineterminator='\n') # Add our own line terminator as it defaults to CRLF otherwise.
        writer.writerows(data_set)

    return True
    