import board
import math
import random
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
    best_moves = []
    for move in possible_moves(board.main_board):
        insert_piece(board.main_board, move, player['cpu'])
        score = minimax(board.main_board, 0, True, player)
        empty_cell(board.main_board, move)
        if score > best_score:
            best_moves.clear()
            best_moves.append(move)
            best_score = score
        elif score == best_score:
            best_moves.append(move)

    #Heuristic
    #Choosing Winning Move
    for move in best_moves:
        insert_piece(board.main_board, move, player['cpu'])
        if check_win(board.main_board)[0] and check_win(board.main_board)[1] == player['cpu']:
            return move
        else:
            empty_cell(board.main_board, move)

    # Check Blocking
    block, index = check_blocks(board.main_board, player)
    if block:
        insert_piece(board.main_board, index, player['cpu'])
        return index

    #Center Cell Availability Test
    for move in best_moves:
        if move == (1, 1):
            insert_piece(board.main_board, move, player['cpu'])
            return move

    if board.main_board[1][1] == player['cpu']:
        high_priority = [item for item in best_moves if item  not in ((0, 0), (0, 2), (2, 0), (2, 2))]
        final_move = random.choice(high_priority)
        insert_piece(board.main_board, final_move, player['cpu'])
        return final_move
    else:
        high_priority = [item for item in best_moves if item in ((0, 0), (0, 2), (2, 0), (2, 2))]
        final_move = random.choice(high_priority)
        insert_piece(board.main_board, final_move, player['cpu'])
        return final_move

def minimax(board, depth, is_maximizer, player):
    win, winner = check_win(board)
    is_draw = check_draw(board)
    if win and winner == player['cpu']:
        return scores[winner]+depth
    elif win and winner == player['human']:
        return scores[winner]-depth
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