import utils


def get_first_solution():
    inpt = utils.read_input("1")
    return sum([1 for diff in [new - old for new, old in zip(inpt[1:], inpt[:-1])] if diff > 0])

def get_second_solution():
    inpt = utils.read_input("1")
    return sum([1 for diff in [(sum(inpt[i-3:i]) - sum(inpt[i-4:i-1])) for i in range(3, len(inpt))] if diff > 0])

print(get_first_solution())
print(get_second_solution())