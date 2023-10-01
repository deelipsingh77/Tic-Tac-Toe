import board
import math
from board import *

scores = {
    'X': None,
    'O': None,
    'tie': 0
}

def set_score(cpu):
    scores[cpu] = 1
    scores['O' if cpu == 'X' else 'X'] = -1

def cpu_move(cpu):
    set_score(cpu)
    best_score = -math.inf
    best_move = None
    for move in possible_moves(board.main_board):
        insert_piece(board.main_board, move, cpu)
        score = minimax(board.main_board, 0, True, cpu)
        empty_cell(board.main_board, move)
        if score > best_score:
            best_score = score
            best_move = move
    insert_piece(board.main_board, best_move, cpu)

def minimax(board, depth, is_maximizer, cpu):
    win, winner = check_win(board)
    is_draw = check_draw(board)
    if win or is_draw:
        if win:
            score = scores.get(winner) # type: ignore
            return score
        elif is_draw:
            score = scores.get('tie')
            return score
    else:
        if is_maximizer:
            best_score = -math.inf
            for move in possible_moves(board):
                insert_piece(board, move, 'O' if cpu == 'X' else 'X')
                score = minimax(board, depth+1, False, 'O' if cpu == 'X' else 'X')
                empty_cell(board, move)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in possible_moves(board):
                insert_piece(board, move, 'O' if cpu == 'X' else 'X')
                score = minimax(board, depth+1, True, 'O' if cpu == 'X' else 'X')
                empty_cell(board, move)
                best_score = min(score, best_score)
            return best_score
