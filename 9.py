import utils

inpt = utils.read_input("9")
inpt = [list(line) for line in inpt]

def is_lower(value, neighbor_values):
    return all([value < neighbor for neighbor in neighbor_values])

def get_first_solution():
    sum = 0
    low_points = []
    for idx in range(len(inpt[0])):
        row = 0
        if idx == 0:
            if is_lower(inpt[row][idx], [inpt[row][idx+1], inpt[row + 1][idx]]):
                sum += int(inpt[row][idx]) + 1
                low_points.append((row, idx))
        elif idx == len(inpt[0]) - 1:
            if is_lower(inpt[row][idx], [inpt[row][idx-1], inpt[row + 1][idx]]):
                sum += int(inpt[row][idx]) + 1
                low_points.append((row, idx))
        else:
            if is_lower(inpt[row][idx], [inpt[row][idx+1], inpt[row][idx-1], inpt[row + 1][idx]]):
                sum += int(inpt[row][idx]) + 1
                low_points.append((row, idx))

        row = len(inpt) - 1
        if idx == 0:
            if is_lower(inpt[row][idx], [inpt[row][idx+1], inpt[row - 1][idx]]):
                sum += int(inpt[row][idx]) + 1
                low_points.append((row, idx))
        elif idx == len(inpt[0]) - 1:
            if is_lower(inpt[row][idx], [inpt[row][idx-1], inpt[row - 1][idx]]):
                sum += int(inpt[row][idx]) + 1
                low_points.append((row, idx))
        else:
            if is_lower(inpt[row][idx], [inpt[row][idx+1], inpt[row][idx-1], inpt[row - 1][idx]]):
                sum += int(inpt[row][idx]) + 1
                low_points.append((row, idx))

        for row in range(1, len(inpt) - 1):
            if idx == 0:
                if is_lower(inpt[row][idx], [inpt[row][idx+1], inpt[row - 1][idx], inpt[row + 1][idx]]):
                    sum += int(inpt[row][idx]) + 1
                    low_points.append((row, idx))
            elif idx == len(inpt[0]) - 1:
                if is_lower(inpt[row][idx], [inpt[row][idx-1], inpt[row - 1][idx], inpt[row + 1][idx]]):
                    sum += int(inpt[row][idx]) + 1
                    low_points.append((row, idx))
            else:
                if is_lower(inpt[row][idx], [inpt[row][idx+1], inpt[row][idx-1], inpt[row - 1][idx], inpt[row + 1][idx]]):
                    sum += int(inpt[row][idx]) + 1
                    low_points.append((row, idx))

    print(sum)
    return low_points

def get_second_solution(low_points):
    basins = []
    for point in low_points:
        basin = set()
        basin.add(point)
        add_neighbouring_points(point, basin)
        basins.append(basin)
    basin_len = [len(basin) for basin in basins]
    basin_len.sort(reverse=True)
    prod = 1
    for basin in basin_len[:3]:
        prod *= basin
    print(prod)

def add_neighbouring_points(point, basin):
    row, idx = point

    if row == 0:
        if idx == 0:
            neighbouring_points = [(row, idx + 1), (row + 1, idx)]
        elif idx == len(inpt[0]) - 1:
            neighbouring_points = [(row, idx - 1), (row + 1, idx)]
        else:
            neighbouring_points = [(row, idx + 1), (row + 1, idx), (row, idx - 1)]
    elif row == len(inpt) - 1:
        if idx == 0:
            neighbouring_points = [(row, idx + 1), (row - 1, idx)]
        elif idx == len(inpt[0]) - 1:
            neighbouring_points = [(row, idx - 1), (row - 1, idx)]
        else:
            neighbouring_points = [(row, idx + 1), (row - 1, idx), (row, idx - 1)]
    else:
        if idx == 0:
            neighbouring_points = [(row, idx + 1), (row + 1, idx), (row - 1, idx)]
        elif idx == len(inpt[0]) - 1:
            neighbouring_points = [(row, idx - 1), (row - 1, idx), (row + 1, idx)]
        else:
            neighbouring_points = [(row, idx - 1), (row - 1, idx), (row + 1, idx), (row, idx + 1)]
            
    valid_neighbours = [neighbour for neighbour in neighbouring_points if (int(inpt[neighbour[0]][neighbour[1]]) != 9 and neighbour not in basin)]
    [basin.add(neighbour) for neighbour in valid_neighbours]
    if len(valid_neighbours) == 0:
        return
    else:
        [add_neighbouring_points(point, basin) for point in valid_neighbours]

if __name__ == "__main__":
    low_points = get_first_solution()
    get_second_solution(low_points)