import utils

class Cuboid:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.intersections = set()

    def intersect(self, other):
        intersection_points = calc_intersection(self, other)
        if intersection_points is not None:
            new_intersection = Cuboid(*intersection_points)
            [intersection.intersect(new_intersection) for intersection in self.intersections]
            self.intersections.add(new_intersection)

    def calc_volume(self):
        xx = self.x[1] + 1 - self.x[0]
        yy = self.y[1] + 1 - self.y[0]
        zz = self.z[1] + 1 - self.z[0]

        return max(0, xx*yy*zz - sum([intersection.calc_volume() for intersection in self.intersections]))

def calc_intersection(c1, c2):

    intersects = True

    x = (max(c1.x[0], c2.x[0]), min(c1.x[1], c2.x[1]))
    if x[1] - x[0] < 0:
        intersects = False

    y = (max(c1.y[0], c2.y[0]), min(c1.y[1], c2.y[1]))
    if y[1] - y[0] < 0:
        intersects = False

    z = (max(c1.z[0], c2.z[0]), min(c1.z[1], c2.z[1]))
    if z[1] - z[0] < 0:
        intersects = False

    if intersects:
        return x, y, z
    else:
        return None

def get_inpt():
    inpt = utils.read_input("22")
    inpt_cleaned = []
    for row in inpt:
        cube = []
        command = row.split(" ")[0]
        row = row.split(" ")[1]
        row = row.split(",")
        for coord in row:
            coord = coord.split("=")[1]
            min = int(coord.split("..")[0])
            max = int(coord.split("..")[1])
            cube.append((min, max))
        inpt_cleaned.append((command, cube))
    return inpt_cleaned

def get_first_solution():
    inpt = get_inpt()
    cuboids = set()
    for row in inpt:
        command = row[0]
        if any([abs(coord) > 50 for axis in row[1] for coord in axis]):
            continue
        new_cuboid = Cuboid(*row[1])
        [cuboid.intersect(new_cuboid) for cuboid in cuboids]
        if command == "on":
            cuboids.add(new_cuboid)

    print(sum([cuboid.calc_volume() for cuboid in cuboids]))
    

def get_second_solution():
    inpt = get_inpt()
    cuboids = set()
    for row in inpt:
        command = row[0]
        new_cuboid = Cuboid(*row[1])
        [cuboid.intersect(new_cuboid) for cuboid in cuboids]
        if command == "on":
            cuboids.add(new_cuboid)

    print(sum([cuboid.calc_volume() for cuboid in cuboids]))


if __name__ == "__main__":
    get_first_solution()
    get_second_solution()