import utils

inpt = utils.read_input("8")

def find_inpt_map(numbers):

    digit_map = [set()] * 10

    for number in numbers.split(" "):
        if len(number) == 2: # 1
            digit_map[1] = set(number)
        elif len(number) == 4: # 4
            digit_map[4] = set(number)
        elif len(number) == 3: # 7
            digit_map[7] = set(number)
        elif len(number) == 7: # 8
            digit_map[8] = set(number)

    for number in numbers.split(" "):
        if len(number) == 5 and len(digit_map[1] - set(number)) == 0: # 3
            digit_map[3] = set(number)
        elif len(number) == 5 and len(set(number) - digit_map[4]) == 2: # 5
            digit_map[5] = set(number)
        elif len(number) == 5: # 2
            digit_map[2] = set(number)

    for number in numbers.split(" "):
        if len(number) == 6 and len(digit_map[1] - set(number)) == 1: # 6
            digit_map[6] = set(number)
        elif len(number) == 6 and len(digit_map[5] - set(number)) == 0: # 9
            digit_map[9] = set(number)
        elif len(number) == 6: # 0
            digit_map[0] = set(number)

    return digit_map

def decode_number(number, digit_map):
    for idx, digit in enumerate(digit_map):
        if set(number) == digit:
            return idx


def get_first_solution():
    inpt_1 = [line.split(" | ")[1] for line in inpt]
    n_digits = 0
    segments = [line.split(" ") for line in inpt_1]
    for line in inpt_1:
        segments = line.split(" ")
        for segment in segments:
            if len(segment) in [2, 3, 4, 7]:
                n_digits += 1
    print(n_digits)


def get_second_solution():
    train = [line.split(" | ")[0] for line in inpt]
    decode = [line.split(" | ")[1] for line in inpt]

    sum = 0
    for train_nums, decode_nums in zip(train, decode):
        digit_map = find_inpt_map(" ".join([train_nums, decode_nums]))
        decoded_number = []
        for number in decode_nums.split(" "):
            decoded_number.append(decode_number(number, digit_map))
        sum+=int("".join([str(x) for x in decoded_number]))
    print(sum)

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()