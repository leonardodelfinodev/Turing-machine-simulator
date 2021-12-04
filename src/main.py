from utils import parse_input as parser

def main():
    instructions = parser.parse_input_file("../examples/example0.txt")
    if type(instructions) == "int":
        print("ok")
    print(instructions)

if __name__ == '__main__':
    main()