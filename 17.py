#target area: x=195..238, y=-93..-67
xmin = 195
xmax = 238

ymin = -93
ymax = -67

def triangular_number(x):
    return x*(x+1)/2

def sum_of_int(start, stop, pos = False):
    if pos:
        return sum([x for x in range(start, stop) if x > 0])
    else:
        return sum(range(start, stop))

def count_x_pos(speed, time):
    return sum([speed - i for i in range(time) if i < speed])

def count_y_pos(speed, time):
    return sum([speed - i for i in range(time)])

def get_first_solution():
    #Part one is solved with math
    print(triangular_number(-ymin - 1))

def get_second_solution():
    max_time = 2 * (-1 * ymin) + 1
    shots = set()
    for time_to_hit in range(1, max_time + 1):
        xx = [x for x in range(1, xmax + 1) if count_x_pos(x, time_to_hit) <= xmax and count_x_pos(x, time_to_hit) >= xmin]
        yy = [y for y in range(ymin, -ymin) if count_y_pos(y, time_to_hit) <= ymax and count_y_pos(y, time_to_hit) >= ymin]
        print("")
        [shots.add((x, y)) for x in xx for y in yy]

    print(len(shots))
    


if __name__ == "__main__":
    get_first_solution()
    get_second_solution()