import os

def read_input(file_name :str):
    input_file = os.path.join(os.getcwd(), "input", file_name + ".txt")
    contents = []
    with open(input_file, 'r') as file:
        contents = [int(val.strip()) for val in file.readlines()]

    return contents