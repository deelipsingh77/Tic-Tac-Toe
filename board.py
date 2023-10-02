class TicTacToeBoard:
    indexes =  {
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
    
    def __init__(self):
        self.board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def insert_piece(self, index, player):
        i, j = TicTacToeBoard.indexes.get(index)
        self.board[i][j] = player

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""

    def indexed_board(self):
        number = 1
        for i in range(3):
            for j in range(3):
                self.board[i][j] = str(number)
                number += 1
        self.print_board()
        self.reset_board()
    
    def print_board(self):
        for i, row in enumerate(self.board):
            for j, item in enumerate(row):
                if not item:
                    item = ' '

                if j < 2:
                    print("",item,"|", end="")
                else:
                    print("",item, end="\n")
            if i < 2:
                print("---|---|---")

    def valid_move(self, index):
        i, j = TicTacToeBoard.indexes.get(index)
        if not self.board[i][j]:
            return True
        else:
            return False

    def check_draw(self):
        return all(all(item for item in row) for row in self.board)

    def empty_cell(self, index):
        i, j = TicTacToeBoard.indexes.get(index)
        self.board[i][j] = ''

    def check_win(self):
        left_diagonal = []
        right_diagonal = []
        for i in range(3):
            left_diagonal.append(self.board[i][i])
            right_diagonal.append(self.board[i][2-i])

        board_transpose = list(map(list, zip(*self.board)))
        combinations = [*self.board, *board_transpose, left_diagonal, right_diagonal]
        for pairs in combinations:
            if pairs[0] == pairs[1] == pairs[2] != '':
                return True, pairs[0]
        return False, None

    def possible_moves(self):
        return [key for key, val in self.indexes.items() if not self.board[val[0]][val[1]]]