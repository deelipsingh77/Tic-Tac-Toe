from board import TicTacToeBoard
from cpu_logic import cpu_move

player = {
    'human': None,
    'cpu': None,
    'turn': True
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

def player_input(board):
    while True:
        cell = input("Enter the cell: ")
        if cell.isnumeric():
            if 0 < int(cell) <= 9:
                if board.valid_move(int(cell)):
                    board.insert_piece(int(cell), player['human'])
                    return True
                else:
                    print("Invalid Move!! Please Choose Again")
                    continue
            else:
                print("Invalid Input!! Please Re-Enter!!")
                continue
        elif cell == '-1':
            print("Thanks for Playing!!😁")
            return False
        else:
            if not cell:
                moves = board.possible_moves()
                if len(moves) == 1:
                    board.insert_piece(moves.pop(), player['human'])
                    return True
                else:
                    print("Invalid Input!! Please Re-Enter!!")
                    continue
            print("Invalid Input!! Please Re-Enter!!!")
            continue

def play():
    running = choose_piece()
    board = TicTacToeBoard()
    
    if running:
        board.indexed_board()

    while running:
        if player['turn']:
            running = player_input(board)
            player['turn'] = not player['turn']
        else:
            move = cpu_move(board, player)
            print("Opponent Played: ", move)
            player['turn'] = not player['turn']

        if board.check_win()[0]:
            board.print_board()
            winner = board.check_win()[1]
            print(f"Winner: {winner}")
            if player['human'] == winner:
                print("Congratulations!! YOU WON.")
            else:
                print("OOPS!! YOU LOST.")
            running = False

        if board.check_draw():
            board.print_board()
            print(f"It's a Tie")
            running = False

        if running:
            board.print_board()

    player.update({
        'human': None,
        'cpu': None,
        'turn': True
    })