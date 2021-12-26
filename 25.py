import utils

def get_inpt():
    inpt = utils.read_input("25")
    south_facing = set()
    east_facing = set()
    for y, line in enumerate(inpt):
        for x, c in enumerate(line):
            if c == ">":
                east_facing.add((x, y))
            elif c == "v":
                south_facing.add((x,y))
    return east_facing, south_facing


def get_first_solution():
    east, south = get_inpt()
    xmax = max({coord[0] for coord in east | south}) + 1
    ymax = max({coord[1] for coord in east | south}) + 1

    i = 0
    done = False

    while not done:
        i += 1

        n_east = set()
        n_south = set()

        #east
        for coord in east:
            new_coord = ((coord[0] + 1) % xmax, coord[1])
            if new_coord not in east and new_coord not in south:
                n_east.add(new_coord)
            else:
                n_east.add(coord)
        #south
        for coord in south:
            new_coord = (coord[0], (coord[1] + 1) % ymax)
            if new_coord not in n_east and new_coord not in south:
                n_south.add(new_coord)
            else:
                n_south.add(coord)

        if south == n_south and east == n_east:
            done = True
        else:
            east = n_east
            south = n_south
            
    return i

if __name__ == "__main__":
    print(get_first_solution())