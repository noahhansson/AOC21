import utils

def parse_inpt():
    inpt = utils.read_input("4")
    start = 0
    idx = 0
    new_inpt = []
    for idx, val in enumerate(inpt):
        if val == "":
            new_inpt.append(inpt[start:idx])
            start = idx + 1
    draws = [int(x) for x in new_inpt[0][0].split(",")]
    boards = [[[int(x) for x in row.split(" ") if x != ""] for row in board] for board in new_inpt[1:]]
    return draws, boards

def check_boards(boards, draws):
    winners = []
    for board in boards:
        diag = [board[i][i] for i in range(5)]
        cols = [board[i] for i in range(5)]
        rows = [board[:][i] for i in range(5)]
        all_entries = [diag] + cols + rows
        for row in all_entries:
            if sum([x in draws for x in row]) == 5:
                winners.append(board)
                boards.remove(board)
                break
    return winners, boards

def count_remaining(board, draws, last_draw):
    s = sum([x for row in board for x in row if x not in draws])
    return s * last_draw

def get_first_solution():
    draws, boards = parse_inpt()
    curr_draws = set()
    for draw in draws:
        curr_draws.add(draw)
        winners, boards = check_boards(boards, curr_draws)
        if len(winners) > 0:
            print(count_remaining(winners[0], curr_draws, draw))
            break

def get_second_solution():
    draws, boards = parse_inpt()
    curr_draws = set()
    winners = []
    for draw in draws:
        curr_draws.add(draw)
        new_winners, boards = check_boards(boards, curr_draws)
        winners += new_winners
        if len(winners) == 99:
            print(count_remaining(winners[-1], curr_draws, draw))
            break
    return None   
            
if __name__ == "__main__":
    get_first_solution()
    get_second_solution()