import utils
import math
from collections import Counter, deque

def get_inpt():
    inpt = utils.read_input("19")
    inpt = [row for row in inpt if row != ""]
    idx_list = [idx for idx, row in enumerate(inpt) if "scanner" in row] + [len(inpt)]
    inpt_per_scanner = [inpt[i+1:j] for i, j in zip(idx_list, idx_list[1:])]
    inpt_per_scanner = [[tuple([int(row.split(",")[0]), int(row.split(",")[1]), int(row.split(",")[2])]) for row in scanner] for scanner in inpt_per_scanner]
    scanners = [Scanner(set(points)) for points in inpt_per_scanner]

    return scanners

class Scanner:
    all_rotations = [
        [0, 0, 0],
        [1, 0, 0],
        [2, 0, 0],
        [3, 0, 0],
        [0, 1, 0],
        [1, 1, 0],
        [2, 1, 0],
        [3, 1, 0],
        [0, 2, 0],
        [1, 2, 0],
        [2, 2, 0],
        [3, 2, 0],
        [0, 3, 0],
        [1, 3, 0],
        [2, 3, 0],
        [3, 3, 0],
        [0, 0, 1],
        [1, 0, 1],
        [2, 0, 1],
        [3, 0, 1],
        [0, 0, 3],
        [1, 0, 3],
        [2, 0, 3],
        [3, 0, 3],
    ]

    def __init__(self, points):
        self.id = create_id()
        self.points = points
        self.x = 0
        self.y = 0
        self.z = 0
        self.rotation = 0

    def offset(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def rotate(self, steps = 1):
        self.rotation = (self.rotation + steps) % len(self.all_rotations)

    def _rotate_3d(self, point, x, y, z):
        point = self._rotate_x(point, x)
        point = self._rotate_y(point, y)
        point = self._rotate_z(point, z)
        return point

    def _rotate_x(self, point, steps):
        cos = int(math.cos(steps * math.pi/2))
        sin = int(math.sin(steps * math.pi/2))
        return tuple([point[0], point[1]*cos - point[2]*sin, point[1]*sin + point[2] * cos])

    def _rotate_y(self, point, steps):
        cos = int(math.cos(steps * math.pi/2))
        sin = int(math.sin(steps * math.pi/2))
        return tuple([point[2]*sin + point[0]*cos, point[1], point[2]*cos - point[0]*sin])

    def _rotate_z(self, point, steps):
        cos = int(math.cos(steps * math.pi/2))
        sin = int(math.sin(steps * math.pi/2))
        return tuple([point[0]*cos - point[1]*sin, point[0]*sin + point[1]*cos, point[2]])

    def get_position(self):
        return tuple([self.x, self.y, self.z])

    def get_points(self):
        #rotate
        points = {self._rotate_3d(point, *self.all_rotations[self.rotation]) for point in self.points}
        #offset
        points = {tuple([point[0] + self.x, point[1] + self.y, point[2] + self.z]) for point in points}

        return points.copy()

    def __repr__(self):
        return "Scanner {}".format(str(self.id))

id = 0
def create_id():
    global id
    ret_id = id
    id += 1
    return ret_id

def offset(p1, p2):
    return (p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2])

def manhattan_dist(p1, p2):
    return abs(p1[0]-p2[0]) +  abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])

def match_scanner(first: Scanner, second: Scanner):
    for _ in range(24):
        dist_vector = [offset(p1, p2) for p2 in second.get_points() for p1 in first.get_points()]
        count = Counter(dist_vector)
        if max(count.values()) >= 12:
            for key, value in count.items():
                if value >= 12:
                    second.offset(*key)
                    overlapping_points = first.get_points() | second.get_points()
                    return Scanner(overlapping_points)
        second.rotate()
    else:
        return None

def match(scanners):
    matched = None
    unmatched = deque(scanners)
    while len(unmatched) > 0:
        candidate = unmatched.popleft()
        if matched is None:
            matched = candidate
        else:
            print("Trying to match", candidate)
            new_matched = match_scanner(matched, candidate)
            if new_matched is not None:
                matched = new_matched
                print("Found a match")
            else:
                print("Did not find a match")
                unmatched.append(candidate)
            print("Remaining scanners:", unmatched)
    return matched

def get_first_solution():
    scanners = get_inpt()
    matched_scanners = match(scanners)
    print(len(matched_scanners.get_points()))

def get_second_solution():
    scanners = get_inpt()
    _ = match(scanners)
    print(max([manhattan_dist(s1.get_position(), s2.get_position()) for s1 in scanners for s2 in scanners]))
    

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()