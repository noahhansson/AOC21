import utils

def get_inpt():
    inpt = utils.read_input("20")

    key = inpt[0]
    key = [1 if c == "#" else 0 for c in key]

    inpt = inpt[1:]
    inpt = [list(row) for row in inpt if row != ""]
    points = set()
    [points.add((x,y)) for x in range(len(inpt)) for y in range(len(inpt[0])) if inpt[x][y] == "#"]
    image = Image(points)

    return image, key

class Image:

    def __init__(self, points, passes = 0):
        self.points = points
        self.passes = passes

        self.xmin = min([point[0] for point in self.points])
        self.xmax = max([point[0] for point in self.points]) + 1
        self.ymin = min([point[1] for point in self.points])
        self.ymax = max([point[1] for point in self.points]) + 1
    
    def _get_code(self, point, key, passes):
        neighbours = [(point[0] + i, point[1] + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]

        if passes % 2 == 0:
            #even iteration, boundary is 0
            values = [1 if neighbour in self.points else 0 for neighbour in neighbours]
        elif passes % 2 == 1:
            #odd iteration, boundary is 1
            outside = lambda x,y : x < self.xmin or x >= self.xmax or y < self.ymin or y >= self.ymax
            values = [1 if neighbour in self.points or outside(*neighbour) else 0 for neighbour in neighbours]
        
        code_binary = "".join([str(x) for x in values])
        code_decimal = int(code_binary, 2)
        value = key[code_decimal]

        return value

    def __repr__(self):
        out = ""
        for x in range(self.xmin, self.xmax):
            for y in range(self.ymin, self.ymax):
                out += "#" if (x,y) in self.points else "-"
            out += "\n"
        return out

    def decode(self, key):
        new_points = set()
        for x in range(self.xmin - 1, self.xmax + 1):
            for y in range(self.ymin - 1, self.ymax + 1):
                value = self._get_code((x,y), key, self.passes)
                if value == 1:
                    new_points.add((x,y))
        image = Image(new_points, self.passes + 1)
        return image

    def get_points(self):
        return self.points

def get_first_solution():
    n_passes = 2
    image, key = get_inpt()
    
    for _ in range(n_passes):
        image = image.decode(key)
    print(image)
    print(len(image.get_points()))

def get_second_solution():
    n_passes = 50
    image, key = get_inpt()
    
    for _ in range(n_passes):
        image = image.decode(key)
    print(image)
    print(len(image.get_points()))

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()