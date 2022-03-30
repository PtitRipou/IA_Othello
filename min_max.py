# -*- coding: utf-8 -*-
# Implémentation de l'algorithme min-max et des fonctions d'évaluations

import gameplay as gp
import othello_board as ob
from math import inf

# Définition de la profondeur maximale
max_depth = 2

# 1ère fonction de l'algorithme min-max -> on manipule ici des tuples (var, k) avec var la valeur d'évaluation et k l'indice d'une position jouable
def max_value(board : 'list[list[int]]', player : 'int', depth : 'int', eval_func : 'function') -> 'tuple':
    var = -inf
    result = (var, -1)
    next_board = gp.next_pos(board, player)
    liste_pos = ob.display_othello(next_board, 1)

    # Conditions de sortie -> profondeur max atteinte ou fin du jeu
    if (depth == max_depth * 2) or (type(gp.end(board, player)) == int):
        return eval_func(board, player)

    # Dans le cas où le joueur ne peux pas jouer -> prochaine étape de l'algorithme
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

# 2ème fonction de l'algorithme min-max -> même particularités que max_value()
def min_value(board : 'list[list[int]]', player : 'int', depth : 'int', eval_func : 'function') -> 'tuple':
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

# Fonction d'évaluation pour la méthode absolue
def fonct_eval_absolu(board : 'list[list[int]]', player : 'int') -> 'tuple':
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

# Fonction d'évaluation pour la méthode positionnelle
def fonct_eval_positional(board : 'list[list[int]]', player : 'int') -> 'tuple':
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

# Fonction d'évaluation pour la méthode mobile -> ici la valeur est une moyenne entre le nombre de coup à jouer et la valeur du poids de la case par rapport aux coins
def fonct_eval_mobility(board : 'list[list[int]]', player : 'int') -> 'tuple':
    next_board = gp.next_pos(board, player)
    liste_pos = ob.display_othello(next_board, 1)
    nb_coup = len(liste_pos)

    val_board = ob.dist_corner()
    nb1, nb2 = 0, 0
    
    for k in board:
        for p in k:

            if p == 1:
                nb1 += val_board[board.index(k)][k.index(p)]
            
            elif p == 2:
                nb2 += val_board[board.index(k)][k.index(p)]
    
    if player == 1:
        res = ((nb1 - nb2) + nb_coup) // 2
        return (res, None)
    
    else:
        res = ((nb2 - nb1) + nb_coup) // 2
        return (res, None)

    return

# Fonction d'évaluation pour la méthode mixte
def fonct_eval_mixed(board : 'list[list[int]]', player : 'int') -> 'tuple':
    res = count_play(board)

    # Nombre de coups restants
    nb_to_play = res[0]

    # Nombre de coups joués
    nb_play = res[1]

    if nb_play < 20:
        return fonct_eval_positional(board, player)
    
    elif nb_to_play < 15:
        return fonct_eval_mobility(board, player)
    
    else:
        return fonct_eval_absolu(board, player)

# Retourne le nombre de cases vides et pleines d'un plateau
def count_play(board : 'list[list[int]]') -> 'tuple':
    nb_empty, nb_full = 0, -4

    for k in board:
        for p in k:
            
            if p == 0:
                nb_empty += 1
            
            else:
                nb_full += 1
    
    return (nb_empty, nb_full)

# 1ère fonction de l'algoritme min-max version alpha-beta -> on manipule toujours les mêmes tuples que dans les fonctions max_value() et min_value()
def max_alpha_beta(board : 'list[list[int]]', player : 'int', depth : 'int', alpha, beta, eval_func : 'function') -> 'tuple':
    var = -inf
    result = (var, -1)
    next_board = gp.next_pos(board, player)
    liste_pos = ob.display_othello(next_board, 1)

    # Test des conditions de sortie -> profondeur max ou fin du jeu
    if (depth == max_depth * 2) or (type(gp.end(board, player)) == int):
        return eval_func(board, player)
    
    # Si le joueur courant ne peut pas jouer de coup -> étape suivante de l'algorithme
    elif len(liste_pos) == 0:

        if player == 1:
            player = 2

        else:
            player = 1

        result_tmp = min_alpha_beta(next_board, player, (depth + 1), alpha, beta, eval_func)

        if result_tmp[0] > result[0]:
            var = result_tmp[0]
            result = (var, -1)
            
        if result_tmp[0] >= beta:
            var = result_tmp[0]
            result = (var, -1)
            return result
            
        if result_tmp[0] > alpha:
            alpha = result_tmp[0]
    
    else:

        for k in range(1, len(liste_pos) + 1):
            next_board2 = gp.next_play(next_board, liste_pos, k, player)

            if player == 1:
                player = 2

            else:
                player = 1

            result_tmp = min_alpha_beta(next_board2, player, (depth + 1), alpha, beta, eval_func)

            if result_tmp[0] > result[0]:
                var = result_tmp[0]
                result = (var, k)
            
            if result_tmp[0] >= beta:
                var = result_tmp[0]
                result = (var, k)
                return result
            
            if result_tmp[0] > alpha:
                alpha = result_tmp[0]

    return result

# 2ème fonction de l'algorithme min-max version alpha-beta -> même particularités que max_alpha_beta()
def min_alpha_beta(board : 'list[list[int]]', player : 'int', depth : 'int', alpha : '+inf', beta : '-inf', eval_func : 'function') -> 'tuple':
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

        result_tmp = max_alpha_beta(next_board, player, (depth + 1), alpha, beta, eval_func)

        if result_tmp[0] < result[0]:
            var = result_tmp[0]
            result = (var, -1)
            
        if result_tmp[0] <= alpha:
            var = result_tmp[0]
            result = (var, -1)
            return result
            
        if result_tmp[0] < beta:
            beta = result_tmp[0]
    
    else:

        for k in range(1, len(liste_pos) + 1):
            next_board2 = gp.next_play(next_board, liste_pos, k, player)

            if player == 1:
                player = 2

            else:
                player = 1

            result_tmp = min_alpha_beta(next_board2, player, (depth + 1), alpha, beta, eval_func)

            if result_tmp[0] < result[0]:
                var = result_tmp[0]
                result = (var, k)
            
            if result_tmp[0] <= alpha:
                var = result_tmp[0]
                result = (var, k)
                return result
            
            if result_tmp[0] < beta:
                beta = result_tmp[0]
    
    return result