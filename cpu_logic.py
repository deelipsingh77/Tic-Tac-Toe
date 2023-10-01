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
        score = minimax(board.main_board, True, player)
        empty_cell(board.main_board, move)
        if score > best_score:
            best_moves.clear()
            best_moves.append(move)
            best_score = score
        elif score == best_score:
            best_moves.append(move)

    print("Best Moves", best_moves) ###
    #Heuristic

    #Choosing Winning Move
    for move in best_moves:
        insert_piece(board.main_board, move, player['cpu'])
        if check_win(board.main_board)[0] and check_win(board.main_board)[1] == player['cpu']:
            print("Winning Move") ###
            return
        else:
            empty_cell(board.main_board, move)

    #Blocking Opponent Win
    for predict_move in best_moves:
        insert_piece(board.main_board, predict_move, player['human'])
        if check_win(board.main_board)[0] and check_win(board.main_board)[1] == player['human']:
            print("Blocked") ###
            empty_cell(board.main_board, predict_move)
            insert_piece(board.main_board, predict_move, player['cpu'])
            return
        else:
            empty_cell(board.main_board, predict_move)

    #Center Cell Availability Test
    for predict_move in best_moves:
        if predict_move == (1, 1):
            print("Center Cell Captured") ###
            insert_piece(board.main_board, predict_move, player['cpu'])
            return
        
    #Corner Cells Availability Test
    final_selection = [move for move in best_moves if move in ((0, 0), (0, 2), (2, 0), (2, 2))]
    if len(final_selection) != 0:
        print("Final Selection: ", final_selection) ###
        insert_piece(board.main_board, random.choice(final_selection), player['cpu'])
        return
    
    insert_piece(board.main_board, random.choice(best_moves), player['cpu'])    

def minimax(board, is_maximizer, player):
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
            score = minimax(board, False, player)
            empty_cell(board, move)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in possible_moves(board):
            insert_piece(board, move, player['cpu'])
            score = minimax(board, True, player)
            empty_cell(board, move)
            best_score = min(score, best_score)
        return best_score
    
# def get_depth(board, move, player):
#     insert_piece(board, move, player['cpu'])
#     depth = minimax(board, 0, True, player)
#     empty_cell(board, move)
#     return depth