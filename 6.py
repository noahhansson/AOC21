import utils

test_inpt = [3,4,3,1,2]
inpt = utils.read_input("6")
inpt = [int(x) for x in inpt[0].split(",")]

def fish_counter(n_days, inp):
    fishes = [0] * 9
    for fish in inp:
        fishes[fish] += 1
    for _ in range(n_days):
        n_new_fishes = fishes[0]
        fishes[:-1] = fishes[1:]
        fishes[8] = n_new_fishes
        fishes[6] += n_new_fishes
    print(sum(fishes))
    
def get_first_solution():
    fish_counter(80, inpt)

def get_second_solution():
    fish_counter(256, inpt)
        
if __name__ == "__main__":
    get_first_solution()
    get_second_solution()