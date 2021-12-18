import math
import utils

inpt = utils.read_input("18")

class Node():
    def __init__(self, string, parent = None):
        self.value = None
        self.left = None
        self.right = None
        self.parent = parent

        if "[" not in string:
            self.value = string
        else:
            left, right = find_left_right(string)
            self.left = Node(left, parent=self)
            self.right = Node(right, parent=self)

    def _reduce(self):
        done = False
        while not done:
            # print(self)
            explosion = self._find_explosion()
            if explosion is not None:
                # print(explosion, "explodes")
                explosion._explode()
            else:
                split = self._find_split()
                if split is not None:
                    # print(split, "splits")
                    split._split()
                else:
                    done = True

    def _find_explosion(self, depth = 4):
        if depth == 0 and self.value is None:
            return self
        elif depth == 0:
            return None

        if self.left is not None:
            left_ex = self.left._find_explosion(depth - 1)
            if left_ex is not None:
                return left_ex

        if self.right is not None:
            right_ex = self.right._find_explosion(depth - 1)
            if right_ex is not None:
                return right_ex

        return None

    def _explode(self):
        left = self._find_left()
        if left is not None:
            left += self.left
        right = self._find_right()
        if right is not None:
            right += self.right

        self.left = None
        self.right = None
        self.value = 0

    def _find_split(self):
        if self.value is not None and int(self.value) > 9:
            return self
        if self.left is not None:
            left_split = self.left._find_split()
            if left_split is not None:
                return left_split
        if self.right is not None:
            right_split = self.right._find_split()
            if right_split is not None:
                return right_split
        return None

    def _split(self):
        left_val = math.floor(int(self.value) / 2)
        right_val = math.ceil(int(self.value) / 2)
        self.left = Node(str(left_val), self)
        self.right = Node(str(right_val), self)
        self.value = None

    def _find_left(self):
        last = self
        search_up = True
        while search_up:
            parent = last.parent
            if parent is None:
                return None
            if parent.left != last:
                search_up = False
            last = parent
        last = last.left
        while True:
            if last.value is not None:
                return last
            last = last.right

    def _find_right(self):
        last = self
        search_up = True
        while search_up:
            parent = last.parent
            if parent is None:
                return None
            if parent.right != last:
                search_up = False
            last = parent
        last = last.right
        while True:
            if last.value is not None:
                return last
            last = last.left

    def _count_magnitude(self):
        if self.value is not None:
            return int(self.value)
        else:
            return 3 * self.left._count_magnitude() + 2 * self.right._count_magnitude()

    def __add__(self, term):
        self.value = str(int(self.value) + int(term.value))

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return "[" + self.left.__str__() + "," + self.right.__str__() + "]"
            
def find_left_right(string):
    layer = 0
    for i, c in enumerate(string):
        if c == "[":
            layer += 1
        elif c == "]":
            layer -= 1
        elif c == "," and layer == 1:
            return string[1:i], string[i+1:-1]


class SnailfishNumber():
    def __init__(self, string):
        self.root = Node(string)
        
    def __str__(self):
        return self.root.__str__()

    def __repr__(self):
        return str(self)

    def __add__(self, term):
        new_number = SnailfishNumber("[{},{}]".format(self, term))
        new_number.root._reduce()

        return new_number

    def count_magnitude(self):
        return self.root._count_magnitude()


test_inpt = [
    "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
    "[[[5,[2,8]],4],[5,[[9,9],0]]]",
    "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
    "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
    "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
    "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
    "[[[[5,4],[7,7]],8],[[8,3],8]]",
    "[[9,3],[[9,9],[6,[4,9]]]]",
    "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
    "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
]

def get_first_solution():
    numbers = [SnailfishNumber(number) for number in inpt]
    sum = numbers[0]
    for number in numbers[1:]:
        sum += number
    print(sum)
    print(sum.count_magnitude())

def get_second_solution():
    combinations = [(x, y) for x in range(len(inpt)) for y in range(len(inpt))]
    print(max((SnailfishNumber(inpt[x]) + SnailfishNumber(inpt[y])).count_magnitude() for x,y in combinations))

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()