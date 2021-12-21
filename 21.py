from functools import lru_cache
from itertools import product

def get_first_solution():
    scores = [0,0]
    positions = [1, 3]
    die = 1
    rolls = 0
    done = False
    while not done:
        for player in range(2):
            positions[player] = (positions[player] + 3 * die + 3 - 1) % 10 + 1
            die = (die + 3 - 1) % 100 + 1
            rolls += 3
            scores[player] += positions[player]
            if any([score >= 1000 for score in scores]):
                done = True
                break

    print(min(scores) * rolls)

@lru_cache(maxsize=None)
def dirac_dice(positions, scores, player):
    if any([score >= 21 for score in scores]):
        if scores[0] >= 21:
            return [1, 0]
        elif scores[1] >= 21:
            return [0, 1]

    roll_dist = {
        3 : 1,
        4 : 3,
        5 : 6,
        6 : 7,
        7 : 6,
        8 : 3,
        9 : 1
    }

    new_games = []
    for roll in roll_dist.keys():
        new_positions = list(positions)
        new_scores = list(scores)
        new_positions[player] = (positions[player] + roll - 1) % 10 + 1
        new_scores[player] = scores[player] + new_positions[player]
        n_outcomes = roll_dist[roll]
        new_games.append((n_outcomes, new_positions, new_scores))

    wins = [0, 0]
    for game in new_games:
        wins = [i + j * game[0] for i, j in zip(wins, dirac_dice(tuple(game[1]), tuple(game[2]), (player + 1) % 2))]
        
    return wins
        
def get_second_solution():
    print(dirac_dice((1, 3), (0, 0), 0))

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()