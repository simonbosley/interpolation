class FileNames:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def get_input_filename(self):
        return self.input_filename
        
    def get_output_filename(self):
        return self.output_filename

# Utility class to read the input and output filenames from the command line arguments array.
class FileNamesArgsReader:
    # Arguments array index constants
    INPUT_FILENAME_INDEX = 1
    OUTPUT_FILENAME_INDEX = 2

    # Useful to record any errors that occured during method 'translate_args'
    last_error = ''
    
    # This method receives a command line arguments string array and returns both input
    # and output filenames in a simple 'FileNames' object.
    @classmethod
    def translate_args(cls, arguments):
        if(len(arguments) == 3):
            return FileNames(arguments[1], arguments[2])
        elif(len(arguments) < 3):
            cls.last_error = f"Not enough command line arguments, please supply input and output file name when running this script."
            return None
        elif(len(arguments) > 3):
            cls.last_error = f"Too many command line arguments, the following arguments were ignored: {arguments[2:]}"
            return None
