import numpy as np
import re
from pathlib import Path

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

# given an input file, extracts the instructions into a list of 5-tuple
def parse_input_file(file):
    if not Path(file).is_file():
        raise IOError("the file does NOT exist.")
    # check if the tuple is valid (any, any, any, any, > or <) -> ignores if there are any errors in the instructions
    regexp = re.compile("\(\s?([^\s]+),\s?([^\s]+),\s?([^\s]+),\s?([^\s]+),\s?([<>-])\)")
    instructions = []
    # every symbol outside the brackets (on same row) will be ignored
    with open(file, "r") as f:
        for line in nonblank_lines(f):
            if regexp.search(line) is None:
                raise Exception("the instruction {0} contains an error.".format(line))
            instructions.append([op.lstrip(' ') for op in line[1:-1].split(",")])
    return np.array(instructions)