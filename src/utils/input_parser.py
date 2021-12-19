import re
from pathlib import Path
from src.exceptions.tuple_exception import TupleException

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

# given an input file, extracts the instructions into a list of 5-tuple
def parse_program(file):
    if not Path(file).is_file():
        raise IOError("the file does NOT exist.")

    # check if the tuple is valid (any, any, any, any, [<, > or -]) -> ignores if there are any errors in the instructions
    # every symbol outside of the brackets (on the same row) will be ignored
    regexp = re.compile("\(\s?([^\s]+),\s?([^\s]+),\s?([^\s]+),\s?([^\s]+),\s?([<>-])\)")
    instructions = []
    with open(file, "r") as f:
        for line in nonblank_lines(f):
            parsed_line = regexp.findall(line)
            if not parsed_line:
                raise TupleException("The instruction: \n\t{0}\n contains an error.".format(line))
            instructions.append(parsed_line[0])
    return instructions
