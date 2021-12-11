import utils

inpt  = utils.read_input("11")
inpt = [[int(digit) for digit in row] for row in inpt]


def increment(grid):
    return [[energy + 1 if energy <9 else 0 for energy in row] for row in grid]

def increment_adj(grid, points):
    for point in points:
        neighbours = [(point[0] + x, point[1] + y) for y in [-1, 0, 1] for x in [-1, 0, 1] if (point[0] + x >= 0) and (point[1] + y >= 0) and (point[0] + x < len(grid)) and (point[1] + y < len(grid))]
        for neighbour in neighbours:
            grid[neighbour[0]][neighbour[1]] += 1
    return grid

def flash(grid):
    flashed = set()
    while any([energy >= 9 for row in grid for energy in row]):
        flashes = [(row, col) for row in range(len(grid)) for col in range(len(grid)) if grid[row][col] >= 9]
        new_flashes = [flash for flash in flashes if flash not in flashed]
        if not new_flashes:
            break
        grid = increment_adj(grid, new_flashes)
        flashed = flashed | set(flashes)
    return grid, len(flashed)

def get_first_solution():
    total_flashes = 0
    grid = inpt.copy()
    for _ in range(100):
        grid, n_flashes = flash(grid)
        total_flashes += n_flashes
        grid = increment(grid)
    print(total_flashes)

def get_second_solution():
    grid = inpt.copy()
    iter = 0
    while True:
        iter+=1
        grid, n_flashes = flash(grid)
        grid = increment(grid)
        if n_flashes == 100:
            break
    print(iter)


if __name__ == "__main__":
    get_first_solution()
    get_second_solution()