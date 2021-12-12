import utils

inpt = utils.read_input("12")
""" inpt = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
] """
start_end = {"start", "end"}
small_caves = set()
large_caves = set()
[(small_caves.add(cave) if cave != cave.upper() else large_caves.add(cave)) for connection in inpt for cave in connection.split("-") if cave not in start_end]

paths = dict()
for cave in (small_caves | large_caves | start_end):
    connections = [connection.split("-")[1] for connection in inpt if connection.split("-")[0] == cave] + [connection.split("-")[0] for connection in inpt if connection.split("-")[1] == cave]
    paths[cave] = connections


def build_path(at, been, all_paths):
    been = been.copy()
    been.append(at)
    if at == "end":
        all_paths.append(been)
    else:
        possible_steps = paths[at]
        possible_steps = [step for step in possible_steps if ((step in small_caves and step not in been) or (step not in small_caves)) and step != "start"]
        if len(possible_steps):
            [build_path(step, been, all_paths) for step in possible_steps]

def build_path2(at, been, n_visits, all_paths):
    been = been.copy()
    n_visits = n_visits.copy()
    n_visits[at] += 1
    been.append(at)
    if at == "end":
        all_paths.append(been)
    else:
        possible_steps = paths[at]
        max_visits = 1 if any(n_visits[cave] > 1 for cave in small_caves) else 2
        possible_steps = [step for step in possible_steps if ((step in small_caves and n_visits[step] < max_visits) or (step not in small_caves)) and step != "start"]
        if len(possible_steps):
            [build_path2(step, been, n_visits, all_paths) for step in possible_steps]

def get_first_solution():
    at = "start"
    been = []
    all_paths = []
    build_path(at, been, all_paths)
    print(len(all_paths))

def get_second_solution():
    at = "start"
    been = []
    all_paths = []
    n_visits = {cave : 0 for cave in small_caves | large_caves | start_end}
    build_path2(at, been, n_visits, all_paths)
    print(len(all_paths))

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()