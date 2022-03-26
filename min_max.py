# -*- coding: utf-8 -*-
# Implémentation de l'algorithme min-max et des fonctions d'évaluations

import gameplay as gp
import othello_board as ob
from math import inf

# Définition de la profondeur maximale
max_depth = 2

def max_value(board : 'list[list[int]]', player : 'int', depth : 'int', eval_func : 'function'):
    var = -inf
    result = (var, -1)
    next_board = gp.next_pos(board, player)
    liste_pos = ob.display_othello(next_board, 1)


    if (depth == max_depth * 2) or (type(gp.end(board, player)) == int):
        return eval_func(board, player)

    elif len(liste_pos) == 0:

        if player == 1:
            player = 2

        else:
            player = 1

        varcomp = min_value(next_board, player, (depth + 1), eval_func)

        if var < varcomp[0]:
            var = varcomp[0]
            result = (var, -1)

    else:

        for k in range(1, len(liste_pos) + 1):
            next_board2 = gp.next_play(next_board, liste_pos, k, player)

            if player == 1:
                player = 2

            else:
                player = 1
            
            varcomp = min_value(next_board2, player, (depth + 1), eval_func)

            if var < varcomp[0]:
                var = varcomp[0]
                result = (var, k)

    return result

def min_value(board : 'list[list[int]]', player : 'int', depth : 'int', eval_func : 'function'):
    var = inf
    result = (var, -1)
    next_board = gp.next_pos(board, player)
    liste_pos = ob.display_othello(next_board, 1)

    if (depth == max_depth * 2) or (type(gp.end(board, player)) == int):
        return eval_func(board, player)

    elif len(liste_pos) == 0:

        if player == 1:
            player = 2

        else:
            player = 1
    
        varcomp = max_value(next_board, player, (depth + 1), eval_func)

        if var > varcomp[0]:
            var = varcomp[0]
            result = (var, -1)

    else:

        for k in range(1, len(liste_pos) + 1):
            next_board2 = gp.next_play(next_board, liste_pos, k, player)

            if player == 1:
                player = 2

            else:
                player = 1
            
            varcomp = max_value(next_board2, player, (depth + 1), eval_func)

            if var > varcomp[0]:
                var = varcomp[0]
                result = (var, k)

    return result

def fonct_eval_absolu(board : 'list[list[int]]', player):
    nb1, nb2 = 0, 0

    for k in board:
        for p in k:

            if p == 1:
                nb1 += 1
            
            elif p == 2:
                nb2 += 1
    
    if player == 1:
        return (nb1 - nb2, None)
    
    else:
        return (nb2 - nb1, None)

def fonct_eval_positional(board : 'list[list[int]]', player):
    val_board = ob.val_board()
    nb1, nb2 = 0, 0

    for k in board:
        for p in k:

            if p == 1:
                nb1 += val_board[board.index(k)][k.index(p)]
            
            elif p == 2:
                nb2 += val_board[board.index(k)][k.index(p)]
    
    if player == 1:
        return (nb1 - nb2, None)
    
    else:
        return (nb2 - nb1, None)