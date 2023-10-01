import board
import math
from board import *

scores = {
    'X': None,
    'O': None,
    'tie': 0
}

def set_score(player):
    scores[player['cpu']] = 1
    scores[player['human']] = -1

def cpu_move(player):
    set_score(player)
    best_score = -math.inf
    best_move = None
    for move in possible_moves(board.main_board):
        insert_piece(board.main_board, move, player['cpu'])
        score = minimax(board.main_board, 0, True, player)
        empty_cell(board.main_board, move)
        if score > best_score:
            best_score = score
            best_move = move
        elif score == best_score:
            current_depth = get_depth(board.main_board, move, player)
            best_depth = get_depth(board.main_board, best_move, player)
            if current_depth < best_depth:
                best_move = move
    insert_piece(board.main_board, best_move, player['cpu'])

def minimax(board, depth, is_maximizer, player):
    win, winner = check_win(board)
    is_draw = check_draw(board)
    if win:
        return scores[winner]
    elif is_draw:
        return scores['tie']
    
    if is_maximizer:
        best_score = -math.inf
        for move in possible_moves(board):
            insert_piece(board, move, player['human'])
            score = minimax(board, depth+1, False, player)
            empty_cell(board, move)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in possible_moves(board):
            insert_piece(board, move, player['cpu'])
            score = minimax(board, depth+1, True, player)
            empty_cell(board, move)
            best_score = min(score, best_score)
        return best_score
    
def get_depth(board, move, player):
    insert_piece(board, move, player['cpu'])
    depth = minimax(board, 0, True, player)
    empty_cell(board, move)
    return depth