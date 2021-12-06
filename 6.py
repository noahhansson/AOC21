import utils

test_inpt = [3,4,3,1,2]
inpt = utils.read_input("6")
inpt = [int(x) for x in inpt[0].split(",")]

def get_first_solution():
    fishes = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for fish in inpt:
        fishes[fish] += 1
    for day in range(1,81):
        n_new_fishes = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]
        fishes[8] = n_new_fishes
        fishes[6] += n_new_fishes
    print(sum(fishes.values()))

def get_second_solution():
    fishes = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for fish in inpt:
        fishes[fish] += 1
    for day in range(1,257):
        n_new_fishes = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]
        fishes[8] = n_new_fishes
        fishes[6] += n_new_fishes
    print(sum(fishes.values()))
        


if __name__ == "__main__":
    get_first_solution()
    get_second_solution()