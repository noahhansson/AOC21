import utils
import heapq
inpt = utils.read_input("15")
inpt_grid = [list(row) for row in inpt]

def dijkstra(start, end, grid):
    costs = {start : 0}
    queue = [(0, start)]
    heapq.heapify(queue)
    while queue:
        cost, pos = heapq.heappop(queue)
        for neighbour in get_neighbours(pos, (len(grid), len(grid[0]))):
            neighbour_cost = cost + int(grid[neighbour[0]][neighbour[1]])
            if neighbour not in costs.keys() or neighbour_cost < costs[neighbour]:
                costs[neighbour] = neighbour_cost
                heapq.heappush(queue, (neighbour_cost, neighbour))
    return costs[end]

def get_neighbours(point, shape):
    neighbours = [(point[0] + i, point[1] + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if abs(i) != abs(j)]
    neighbours = [neighbour for neighbour in neighbours if not (neighbour[0] < 0 or neighbour[0] >= shape[0] or neighbour[1] < 0 or neighbour[1] >= shape[1])]
    return neighbours

def get_first_solution():
    print(dijkstra((0,0), (len(inpt_grid) - 1, len(inpt_grid[0]) - 1), inpt_grid))

def get_second_solution():
    new_grid = [[0 for _ in range(len(inpt_grid[0]) * 5)] for _ in range(len(inpt_grid) * 5)]
    for x in range(len(new_grid)):
        for y in range(len(new_grid[x])):
            new_grid[x][y] = (int(inpt_grid[x % len(inpt_grid)][y % len(inpt_grid[0])]) + y // len(inpt_grid[0]) + x // len(inpt_grid) - 1) % 9 + 1

    print(dijkstra((0,0), (len(new_grid) - 1, len(new_grid[0]) - 1), new_grid))

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()