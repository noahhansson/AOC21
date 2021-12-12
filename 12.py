import utils

inpt = utils.read_input("12")
start_end = {"start", "end"}
small_caves = set()
large_caves = set()
[(small_caves.add(cave) if cave != cave.upper() else large_caves.add(cave)) for connection in inpt for cave in connection.split("-") if cave not in start_end]

paths = dict()
for cave in (small_caves | large_caves | start_end):
    connections = [connection.split("-")[1] for connection in inpt if connection.split("-")[0] == cave] + [connection.split("-")[0] for connection in inpt if connection.split("-")[1] == cave]
    paths[cave] = connections


def build_path1(at = "start", been = [], n_visits =  {cave : 0 for cave in small_caves | large_caves | start_end}, all_paths = []):
    been = been.copy()
    n_visits = n_visits.copy()
    n_visits[at] += 1
    been.append(at)
    if at == "end":
        all_paths.append(been)
    else:
        possible_steps = paths[at]
        max_visits = 1
        possible_steps = [step for step in possible_steps if ((step in small_caves and n_visits[step] < max_visits) or (step not in small_caves)) and step != "start"]
        if len(possible_steps):
            [build_path1(step, been, n_visits, all_paths) for step in possible_steps]

def build_path2(at = "start", been = [], n_visits =  {cave : 0 for cave in small_caves | large_caves | start_end}, all_paths = []):
    been = been.copy()
    n_visits = n_visits.copy()
    n_visits[at] += 1
    been.append(at)
    if at == "end":
        all_paths.append(been)
    else:
        possible_steps = paths[at]
        max_visits = 2 if all(n_visits[cave] < 2 for cave in small_caves) else 1
        possible_steps = [step for step in possible_steps if ((step in small_caves and n_visits[step] < max_visits) or (step not in small_caves)) and step != "start"]
        if len(possible_steps):
            [build_path2(step, been, n_visits, all_paths) for step in possible_steps]

def get_first_solution():
    all_paths = []
    build_path1(all_paths = all_paths)
    print(len(all_paths))

def get_second_solution():
    all_paths = []
    build_path2(all_paths = all_paths)
    print(len(all_paths))

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()