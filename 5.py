import utils

def range_plus(start, stop, step = 1):
    #Extends the range iterator to handle negative differences natively
    if start > stop: return range(start, stop - 1, -step)
    else: return range(start, stop + 1, step)

def get_first_solution():
    inpt = [[tuple(coord.split(",")) for coord in line.split(" -> ")] for line in utils.read_input("5")]
    coords = dict()
    #Straight lines
    for line in [line for line in inpt if (line[0][0] == line[1][0]) or (line[0][1] == line[1][1])]:
        for x in range_plus(int(line[0][0]), int(line[1][0])):
             for y in range_plus(int(line[0][1]), int(line[1][1])):
                 if (x, y) not in coords.keys(): coords[(x, y)] = 1 
                 else: coords[(x, y)] += 1
    overlaps = [(key, value) for key, value in coords.items() if value > 1]
    print(len(overlaps))
    
def get_second_solution():
    inpt = [[tuple(coord.split(",")) for coord in line.split(" -> ")] for line in utils.read_input("5")]
    coords = dict()
    #Straight lines
    for line in [line for line in inpt if (line[0][0] == line[1][0]) or (line[0][1] == line[1][1])]:
        for x in range_plus(int(line[0][0]), int(line[1][0])):
             for y in range_plus(int(line[0][1]), int(line[1][1])):                 
                 if (x, y) not in coords.keys(): coords[(x, y)] = 1 
                 else: coords[(x, y)] += 1
    #Diagonal lines
    for line in [line for line in inpt if not ((line[0][0] == line[1][0]) or (line[0][1] == line[1][1]))]:
        for x, y in zip(range_plus(int(line[0][0]), int(line[1][0])), range_plus(int(line[0][1]), int(line[1][1]))):
            if (x, y) not in coords.keys(): coords[(x, y)] = 1 
            else: coords[(x, y)] += 1
    overlaps = [(key, value) for key, value in coords.items() if value > 1]
    print(len(overlaps))

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()