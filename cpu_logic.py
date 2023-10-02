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
        score = minimax(board.main_board, 0, False, player)
        empty_cell(board.main_board, move)
        if score > best_score:
            best_score = score
            best_move = move
    insert_piece(board.main_board, best_move, player['cpu'])
    return best_move

def minimax(board, depth, is_maximizer, player):
    win, winner = check_win(board)
    is_draw = check_draw(board)
    if win and winner == player['cpu']:
        return scores[winner]*(len(possible_moves(board))+1)
    elif win and winner == player['human']:
        return scores[winner]*(len(possible_moves(board))+1)
    elif is_draw:
        return scores['tie']
    
    if is_maximizer:
        best_score = -math.inf
        for move in possible_moves(board):
            insert_piece(board, move, player['cpu'])
            score = minimax(board, depth+1, False, player)
            empty_cell(board, move)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in possible_moves(board):
            insert_piece(board, move, player['human'])
            score = minimax(board, depth+1, True, player)
            empty_cell(board, move)
            best_score = min(score, best_score)
        return best_score