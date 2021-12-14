import utils
from collections import defaultdict

def get_inpt():
    inpt = utils.read_input("14")
    start_line = inpt[0]
    start_line_pairs = [start_line[i] + start_line[i + 1] for i in range(len(start_line) - 1)] 
    reactions_dict = {line[:2] : [line[0] + line[-1:], line[-1:] + line[1]] for line in inpt[2:]}
    pairs_dict = defaultdict(int)
    for pair in start_line_pairs:
        pairs_dict[pair] += 1

    first = start_line[0]
    last = start_line[-1]

    return pairs_dict, reactions_dict, first, last

def count_chemicals(pairs, first, last):
    count = defaultdict(int)
    for key, val in pairs.items():
        count[key[0]] += val / 2
        count[key[1]] += val / 2
    for key in [first, last]:
        count[key] += 1/2
    return count

def react(pair_dict, reactions_dict):
    out_pairs = defaultdict(int)
    for pair, val in pair_dict.items():
        for out_pair in reactions_dict[pair]:
            out_pairs[out_pair] += val
    return out_pairs

def get_first_solution():
    pairs, reactions, first, last = get_inpt()
    for _ in range(10):
        pairs = react(pairs, reactions)
    count = count_chemicals(pairs, first, last)
    print(max(count.values()) - min(count.values()))

def get_second_solution():
    pairs, reactions, first, last = get_inpt()
    for _ in range(40):
        pairs = react(pairs, reactions)
    count = count_chemicals(pairs, first, last)
    print(max(count.values()) - min(count.values()))

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()