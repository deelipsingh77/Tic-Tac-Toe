main_board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]

indexes = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

def insert_piece(board, index, player):
    board[index[0]][index[1]] = player

def reset_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ""

def indexed_board(board):
    number = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = number
            number += 1
    print_board(board)
    reset_board(board)
    
def print_board(board):
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if not item:
                item = ' '

            if j < 2:
                print("",item,"|", end="")
            else:
                print("",item, end="\n")
        if i < 2:
            print("-----------")

def valid_move(board, index):
    if not board[index[0]][index[1]]:
        return True
    else:
        return False

def check_draw(board):
    return all(all(item for item in row) for row in board)

def empty_cell(board, index):
    board[index[0]][index[1]] = ''

def check_win(board):
    left_diagonal = []
    right_diagonal = []
    for i in range(3):
        left_diagonal.append(board[i][i])
        right_diagonal.append(board[i][2-i])

    board_transpose = list(map(list, zip(*board)))
    combinations = [*board, *board_transpose, left_diagonal, right_diagonal]
    for pairs in combinations:
        if pairs[0] == pairs[1] == pairs[2] != '':
            return True, pairs[0]
    return False, None

def possible_moves(board):
    moves = []
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if not item:
                moves.append((i, j))
    return moves