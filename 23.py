from copy import deepcopy
import heapq
import time

class maxsize_stack(list):

    def __init__(self, maxsize):
        super().__init__()
        self.maxsize = maxsize

    def append(self, obj):
        if len(self) < self.maxsize:
            super().append(obj)
        else:
            raise ValueError("Tried to append {} to a full stack".format(obj))

    def peek(self):
        if len(self) > 0:
            return self[-1]
        else:
            return None

    def isfull(self):
        return len(self) == self.maxsize

    def __str__(self):
        return str(self + [" "] * (self.maxsize - len(self)))

    def __repr__(self):
        return str(self)

class Burrow:
    costs = {
        "A" : 1,
        "B" : 10,
        "C" : 100,
        "D" : 1000
    }

    rooms = {
        "A" : 2,
        "B" : 4,
        "C" : 6,
        "D" : 8
    }

    def __init__(self, positions, depth):
        self.depth = depth
        self.positions = [maxsize_stack(depth + 1) if i in [2, 4, 6, 8] else maxsize_stack(1) for i in range(11)]

        for i, position in enumerate([2, 4, 6, 8]):
            for value in positions[i]:
                self.positions[position].append(value)

    def is_sorted(self):
        if (all([len(self.positions[i]) == 0 for i in [0, 1, 3, 5, 7, 9, 10]]) and
            all([self.positions[self.rooms[val]][1:] == [val] * self.depth for val in ["A","B","C","D"]])
        ):
            return True
        else:
            return False

    def move(self, from_idx, to_idx):

        burrow = self.copy()

        #Distance to move in corridor
        dist = abs(from_idx - to_idx)
        #Distance to move out of room
        dist += burrow.positions[from_idx].maxsize - len(burrow.positions[from_idx])
        #Distance to move into room
        dist += burrow.positions[to_idx].maxsize - len(burrow.positions[to_idx]) - 1

        val = burrow.positions[from_idx].pop()
        burrow.positions[to_idx].append(val)
        cost = dist * burrow.costs[val]
        # print("Moved {} from position {} to {}. Cost = {}".format(val, from_idx, to_idx, cost))

        return burrow, cost

    def get_moves(self, from_idx):
        moves = set()

        amphipod_type = self.positions[from_idx].peek()

        if amphipod_type is None:
            #Nothing to move from here
            return set()

        if from_idx in [2, 4, 6, 8] and all([from_idx == self.rooms[val] for val in self.positions[from_idx]]):
            #Amphipod is in the correct room and should not be moved
            return set()

        #Search for empty spaces downards
        for i in range(11 - from_idx + 1, 12):
            if self.positions[11 - i].isfull():
                break
            else:
                moves.add(11-i)

        #Search for empty spaces upwards
        for i in range(from_idx + 1, 11):
            if self.positions[i].isfull():
                break
            else:
                moves.add(i)

        for position in [2, 4, 6, 8]:
            if position in moves:
                #If target room is not the correct one
                if (self.rooms[amphipod_type] != position
                #If the target room is the correct one but the wrong amphipod type is already in it
                or (self.positions[position].peek() is not None and any([position != self.rooms[val] for val in self.positions[position]]))):
                    moves.remove(position)

        if from_idx in [0, 1, 3, 5, 7, 9, 11]:
            #Only move from corridor to room
            moves = {move for move in moves if move in [2, 4, 6, 8]}


        return moves

    def get_connected(self):
        states = []
        for i in range(11):
            for move in self.get_moves(i):
                new_burrow, cost = self.move(i, move)
                states.append((cost, new_burrow))

        return states
        

    def display(self):
        empty = " "
        positions = deepcopy(self.positions)
        for position in positions:
            for _ in range(position.maxsize - len(position)):
                position.append(empty)
        out = ""
        for position in positions[::-1]:
            out += str(position[::-1])
            out += "\n"
        print(out)

    def __str__(self):
        return "".join([str(pos) for pos in self.positions])

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return 1

    def copy(self):
        return deepcopy(self)

def dijkstra(start_burrow, target = None):
    queue = [(0, start_burrow)]
    seen = set()
    heapq.heapify(queue)
    while queue:
        cost, burrow = heapq.heappop(queue)
        if burrow == target:
            return cost
        if burrow in seen:
            continue
        seen.add(burrow)
        for state in burrow.get_connected():
            heapq.heappush(queue, (cost + state[0], state[1]))

    print("No solution found")
    return 0


def get_first_solution():
    start = time.time()
    burrow = Burrow([["D", "B"], 
                    ["D", "C"], 
                    ["A", "C"], 
                    ["A", "B"]], 
                    2)

    target = Burrow([["A", "A"], ["B", "B"], ["C", "C"], ["D", "D"]], 2)
    print(dijkstra(burrow, target))
    print("Time taken: {}".format((time.time() - start)))

def get_second_solution():
    start = time.time()
    burrow = Burrow([["D", "D", "D", "B"], 
                    ["D", "B", "C", "C"], 
                    ["A", "A", "B", "C"], 
                    ["A", "C", "A", "B"]], 
                    4)
                    
    target = Burrow([["A", "A", "A", "A"], 
                    ["B", "B", "B", "B"], 
                    ["C", "C", "C", "C"], 
                    ["D", "D", "D", "D"]], 
                    4)
    print(dijkstra(burrow, target))
    print("Time taken: {}".format((time.time() - start)))

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()