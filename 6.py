import utils

test_inpt = [3,4,3,1,2]
inpt = utils.read_input("6")
inpt = [int(x) for x in inpt[0].split(",")]

def fish_counter(n_days, inp):
    fishes = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for fish in inp:
        fishes[fish] += 1
    for day in range(1,n_days + 1):
        n_new_fishes = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]
        fishes[8] = n_new_fishes
        fishes[6] += n_new_fishes
    print(sum(fishes.values()))
    
def get_first_solution():
    fish_counter(80, inpt)

def get_second_solution():
    fish_counter(256, inpt)
        


if __name__ == "__main__":
    get_first_solution()
    get_second_solution()