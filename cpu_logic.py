import math
import random

scores = {
    'X': None,
    'O': None,
    'tie': 0
}

def set_score(player):
    scores.update({
        player['cpu']: 1,
        player['human']: -1
    })

def cpu_move(board, player):
    set_score(player)
    best_score = -math.inf
    best_move = []
    for move in board.possible_moves():
        board.insert_piece(move, player['cpu'])
        score = minimax(board, 0, False, player)
        board.empty_cell(move)
        if score > best_score:
            best_score = score
            best_move.clear()
            best_move.append(move)
        elif score == best_score:
            best_move.append(move)
    choice = random.choice(best_move)
    board.insert_piece(choice, player['cpu'])
    return choice

def minimax(board, depth, is_maximizer, player):
    win, winner = board.check_win()
    is_draw = board.check_draw()
    if win and winner == player['cpu']:
        return scores[player['cpu']] * (len(board.possible_moves())+1)
    elif win and winner == player['human']:
        return scores[player['human']] * (len(board.possible_moves())+1)
    elif is_draw:
        return scores.get('tie')
    
    best_score = -math.inf if is_maximizer else math.inf
    for move in board.possible_moves():
        board.insert_piece(move, player['cpu'] if is_maximizer else player['human'])
        score = minimax(board, depth+1, False if is_maximizer else True, player)
        board.empty_cell(move)
        best_score = max(score, best_score) if is_maximizer else min(score, best_score)
    return best_score