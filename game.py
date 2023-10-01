import board
from board import *
from cpu_logic import cpu_move

turn = True
player = {
    'human': None,
    'cpu': None
}

def choose_piece():
    while not player['human']:
        piece = input("Choose O or X: ").upper()
        if piece not in ('O', 'X'):
            if piece == '-1':
                print("Thanks for Playing!!😁")
                return False
                
            print("Invalid Choice!!")
        else:
            player['human'] = piece
    
    player['cpu'] = 'O' if player['human'] == 'X' else 'X'
    return True

def player_input():
    while True:
        cell = input("Enter the cell: ")
        if cell.isnumeric():
            if 0 < int(cell) <= 9:
                index = indexes[int(cell)]
                if valid_move(board.main_board, index):
                    insert_piece(board.main_board, index, player['human'])
                else:
                    print("Invalid Move!! Please Choose Again")
                    continue
                return True
            else:
                print("Invalid Input!! Please Re-Enter!!")
                continue
        elif cell == '-1':
            print("Thanks for Playing!!😁")
            return False
        else:
            if not cell:
                moves = possible_moves(board.main_board)
                if len(moves) == 1:
                    insert_piece(board.main_board, moves.pop(), player['human'])
                    return True
                else:
                    print("Invalid Input!! Please Re-Enter!!")
                    continue
            print("Invalid Input!! Please Re-Enter!!!")
            continue

def play():
    global turn

    running = choose_piece()
    indexed_board(board.main_board) if running else None

    while running:
        if turn:
            running = player_input()
            turn = not turn
        else:
            move = cpu_move(player)
            for key, val in indexes.items():
                if move == val:
                    cell_number = key

            print("Opponent Played: ", cell_number)
            turn = not turn

        if check_win(board.main_board)[0]:
            print_board(board.main_board)
            winner = check_win(board.main_board)[1]
            print(f"Winner: {winner}")
            if player['human'] == winner:
                print("Congratulations!! YOU WON.")
            else:
                print("OOPS!! YOU LOST.")
            running = False

        if check_draw(board.main_board):
            print_board(board.main_board)
            print(f"It's a Tie")
            running = False

        print_board(board.main_board) if running else None

    turn = True
    player['human'] = None
    player['cpu'] = None