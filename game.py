import board
from board import *
from cpu_logic import cpu_move

human = None
cpu = None
turn = True

def choose_piece():
    global human, cpu
    while not human:
        piece = input("Choose O or X: ").upper()
        if piece not in ('O', 'X'):
            if piece == '-1':
                print("Thanks for Playing!!😁")
                return False
                
            print("Invalid Choice!!")
        else:
            human = piece
    
    cpu = 'O' if human == 'X' else 'X'
    return True

def player_input():
    while True:
        cell = input("Enter the cell: ")
        if cell.isnumeric():
            if 0 < int(cell) <= 9:
                index = indexes[int(cell)]
                if valid_move(board.main_board, index):
                    insert_piece(board.main_board, index, human)
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
                    insert_piece(board.main_board, moves.pop(), human)
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
            cpu_move(cpu)
            turn = not turn

        if check_win(board.main_board)[0]:
            print_board(board.main_board)
            print(f"Winner: {check_win(board.main_board)[1]}")
            running = False
            continue

        if check_draw(board.main_board):
            print_board(board.main_board)
            print(f"It's a Tie")
            running = False
            continue

        print_board(board.main_board) if running else None
        