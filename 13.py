import utils

inpt = utils.read_input("13")
points = {tuple(int(num) for num in point.split(",")) for point in inpt if "fold" not in point and point != ""}
instructions = [tuple([instruction.strip("fold along ").split("=")[0], int(instruction.strip("fold along ").split("=")[1])]) for instruction in inpt if "fold" in instruction]

class OrigamiPaper:
    def __init__(self, points):
        self.points = points

    def fold(self, axis, index):
        to_remove = set()
        to_add = set()
        for point in self.points:
            if axis == "x":
                if point[0] > index:
                    to_remove.add(point)
                    to_add.add((2 * index - point[0], point[1]))
            elif axis == "y":
                if point[1] > index:
                    to_remove.add(point)
                    to_add.add((point[0], 2 * index - point[1]))
        [self.points.remove(point) for point in to_remove]
        [self.points.add(point) for point in to_add]

    def get_points(self):
        return self.points

    def __repr__(self):
        max_x = max([point[0] for point in self.points])
        max_y = max([point[1] for point in self.points])
        out = ""
        for y in range(max_y + 1):
            out += "".join(["#" if (x, y) in self.points else " " for x in range(max_x + 1)])
            out += "\n"
        return out

def get_first_solution():
    paper = OrigamiPaper(points)
    instruction = instructions[0]
    paper.fold(*instruction)
    print(len(paper.get_points()))

def get_second_solution():
    paper = OrigamiPaper(points)
    for instruction in instructions:
        paper.fold(*instruction)
    print(paper)

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()