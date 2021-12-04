# given an input file, extract the instructions into a list of 5-tuple
def parse_input_file(file):
    # check if the file exists
    with open(file, "r") as f:
        # TODO:
        # for each line in the file, check if the 5-tuple is valid (regexp?)
        # if it is, insert it into a numpy array
        # if it's not, return an error

        # every symbol outside the brackets (same row) will be ignored

        # skip empty lines
        pass