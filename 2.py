import utils


def get_first_solution():
    inpt = utils.read_input("2")
    route = {
        "forward" : 0,
        "up" : 0,
        "down" : 0
    }
    for command in inpt:
        direction, steps = command.split(" ")
        route[direction] += int(steps)
    print(route["forward"] * abs(route["up"] - route["down"]))

def get_second_solution():
    inpt = utils.read_input("2")
    aim = 0
    route = {
        "position" : 0,
        "depth" : 0
    }
    for command in inpt:
        direction, steps = command.split(" ")
        if direction == "up":
            aim -= int(steps)
        elif direction == "down":
            aim += int(steps)
        elif direction == "forward":
            route["position"] += int(steps)
            route["depth"] += int(steps) * aim
    print(route)
    print(route["position"] * abs(route["depth"]))


if __name__ == "__main__":
    get_first_solution()
    get_second_solution()