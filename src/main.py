import pathlib
from utils.input_parser import parse_program
from src.exceptions.tuple_exception import TupleException

from src.logic.MdT import TuringMachine

def main():
    """
    n_files = 0
    for path in pathlib.Path("../examples").iterdir():
        if path.is_file():
            n_files += 1

    for file in range(n_files):
        try:
            for instruction in parse_program("../examples/example{}.txt".format(file)):
                print(instruction)
        except TupleException as e:
            print(e)
        print()
    """
    try:
        instructions = parse_program("../examples/example4.txt")
    except TupleException as e:
        print(e)
        return

if __name__ == "__main__":
    main()