import pathlib
from termcolor import colored
from utils import input_parser as parser

# TODO: custom exception for the examples (SyntaxException)
def main():
    n_files = 0
    for path in pathlib.Path("../examples").iterdir():
        if path.is_file():
            n_files += 1

    for file in range(n_files):
        try:
            instructions = parser.parse_input_file("../examples/example{0}.txt".format(file))
        except Exception as e:
            print(colored(e.args, "red"))
            print()
            continue
        print(colored("Example n. {0}".format(file+1), "magenta"))
        for instruction in instructions:
            print(colored(instruction, "green"))
        print()

if __name__ == '__main__':
    main()