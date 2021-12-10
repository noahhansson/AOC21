import utils

inpt = utils.read_input("10")

brackets = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">",
}

scores1 = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137,
}

scores2 = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4,
}


def get_first_solution():
    score = 0
    for line in inpt:
        stack = []
        for char in line:
            if char in brackets.keys():
                stack.append(char)
            else:
                if not char == brackets[stack.pop()]:
                    score += scores1[char]
                    break

    print(score)

def get_second_solution():
    score = []
    for line in inpt:
        corrupted = False
        stack = []
        for char in line:
            if char in brackets.keys():
                stack.append(char)
            else:
                if not char == brackets[stack.pop()]:
                    corrupted = True
        if not corrupted:
            line_score = 0
            for char in stack[::-1]:
                line_score *=5
                line_score += scores2[brackets[char]]
            score.append(line_score)
        

    print(sorted(score)[len(score) // 2])

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()