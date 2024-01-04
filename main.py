from lexer import lexer
from parser1 import parser


try:
    with open("input_file.txt", "r") as file: #give your filename
        data = file.read()
        print("File Content:")
        print(data)
        parser.parse(data, lexer=lexer)
        print("Parsing successful!")

except Exception as e:
    print(f"Error during parsing: {e}")
