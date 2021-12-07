import utils
import matplotlib.pyplot as plt

inpt = utils.read_input("7")
inpt = [int(val) for val in inpt[0].split(",")]

test_inpt = [16,1,2,0,4,2,7,1,2,14]


def get_first_solution():
    best_pos_fuel = 10000000000000

    for pos in range(len(inpt)):
        fuel_cost = sum([abs(x - pos) for x in inpt])
        if fuel_cost < best_pos_fuel:
            best_pos_fuel = fuel_cost

    print(best_pos_fuel)

def get_second_solution():
    best_pos_fuel = 10000000000000

    for pos in range(len(inpt)):
        fuel_cost = sum([sum(range(abs(x - pos)+1)) for x in inpt])
        if fuel_cost < best_pos_fuel:
            best_pos_fuel = fuel_cost

    print(best_pos_fuel)



if __name__ == "__main__":
    get_first_solution()
    get_second_solution()