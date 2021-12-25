from typing import TextIO
import re
from pathlib import Path
from src.exceptions.tuple_exception import TupleException

def nonblank_lines(file: TextIO) -> TextIO:
    for l in file:
        line = l.rstrip()
        if line:
            yield line


# (0, 0..9+, 0, 0..9+, >)
# (0, A..J-, ADD, A..J-, <)
# 0, STATE, STATE[12345], STATE[0..9]
# TODO: unpack each instruction
def unpack_instruction(instruction: tuple[str, str, str, str, str]) -> list[tuple[str, str, str, str, str]]:
    current_state, current_symbol, next_state, next_symbol, direction = instruction

    if ("[" in current_state) and ("]" in current_state):
        pass

    return [(current_state, current_symbol, next_state, next_symbol, direction)]


# given an input file, extracts the instructions into a list of 5-tuple
def parse_program(file: str) -> list[tuple[str, str, str, str, str]]:
    if not Path(file).is_file():
        raise IOError("the file does NOT exist.")

    # check if the tuple is valid (any, any, any, any, [<, > or -]) -> ignores if there are any errors in the instructions
    # every symbol outside the brackets (on the same row) will be ignored
    regexp = re.compile("\(\s?([^\s]+),\s?([^\s]+),\s?([^\s]+),\s?([^\s]+),\s?([<>-])\)")
    instructions = []
    with open(file, "r") as f:
        for line in nonblank_lines(f):
            parsed_line = regexp.findall(line)
            if not parsed_line:
                raise TupleException("The instruction: \n\t{0}\n contains an error.".format(line))
            instructions.extend(unpack_instruction(parsed_line[0]))
    return instructions
