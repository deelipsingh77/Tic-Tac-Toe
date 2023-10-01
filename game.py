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
            print("Invalid Choice!!")
        else:
            human = piece
    
    cpu = 'O' if human == 'X' else 'X'

def player_input():
    while True:
        # Testing
        # global human, cpu
        cell = input("Enter the cell: ")
        if cell.isnumeric():
            if 0 < int(cell) <= 9:
                index = indexes[int(cell)]
                if valid_move(board.main_board, index):
                    insert_piece(board.main_board, index, human)
                else:
                    print("Invalid Move!! Please Choose Again")
                    continue
                # Testing
                # human, cpu = cpu, human
                return True
            else:
                print("Invalid Input!! Please Re-Enter!!")
                continue
        elif cell == '-1':
            print("Thanks for Playing!!😁")
            return False
        else:
            print("Invalid Input!! Please Re-Enter!!!")
            continue

def play():
    global turn
    choose_piece()
    indexed_board(board.main_board)

    running = True
    while running:
        if turn:
            running = player_input()
            turn = not turn
        else:
            # running = player_input()
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

        print_board(board.main_board)
        