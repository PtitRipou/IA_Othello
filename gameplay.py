# -*- coding: utf-8 -*-
# Implémentation des instrunctions de jeu

import othello_board as ob
import copy

# Permet de déterminer les positions suivantes possible pour une configuration de plateau
def next_pos(board : 'list[list[int]]', player : 'int') -> 'list[list[int]]':
    next_board = copy.deepcopy(board)

    for k in range(8):

        for p in range(8):
            
            # Si le pion appartient au joueur courant, regarder si un coup est jouable
            if board[k][p] == player:
                list_play = list_possible_play(board, k, p, player)
                
                # Si un ou plusieurs coups sont jouables, remplacer la / les cases corresponndantes sur le plateau par la valeur 3
                if list_play != []:

                    for i in range(len(list_play)):
                        next_board[list_play[i][0]][list_play[i][1]] = 3

    return next_board

# Détermine si le pion positionné en p,k permet de jouer un coup (analyse les pions voisins)
def list_possible_play(board : 'list[list[int]]', k : 'int', p : 'int', player : 'int') -> 'list':
    pos_k = [-1,-1,-1,0,0,1,1,1]
    pos_p = [-1,0,1,-1,1,-1,0,1]
    list_play = []

    # Parcours des positions voisines
    for i in range(8):
        k2 = k + pos_k[i]
        p2 = p + pos_p[i]

        # Test de sortie de plateau
        if k2 < 0 or p2 < 0 or k2 > 7 or p2 > 7:
            continue

        else:

            if board[k2][p2] == 0:
                continue

            elif board[k2][p2] == player:
                continue
            
            # Si la case voisine contient un pion du joueur adverse -> regarder si le coup est jouable
            else:
                var = how_far(board, pos_k[i], pos_p[i], k2, p2, player)
                
                if var == False:
                    continue

                else:
                    list_play.append(var)

    return list_play

# Permet de savoir, lorsqu'un pion est voisin d'un pion adverse, si un coup est jouable
def how_far(board : 'list[list[int]]', ind_k : 'int', ind_p : 'int', k : 'int', p : 'int', player : 'int') -> 'list[int] or False':
    var1 = True
    var2 = 0

    # Recherche dans l'axe du pion voisin les conditions pour jouer un coup
    while var1 == True:
        var2 += 1
        k2 = k + ind_k * var2
        p2 = p + ind_p * var2

        if k2 < 0 or p2 < 0 or k2 > 7 or p2 > 7:
            break

        elif board[k2][p2] == player:
            break

        elif (board[k2][p2] == 0):
            return [k2, p2]

    return False

# Permet de jouer un coup
def next_play(board : 'list[list[int]]', liste_pos : 'list[tuple]', pos : 'int', player : 'int') -> 'list[list[int]]':
    pos_k = [-1,-1,-1,0,0,1,1,1]
    pos_p = [-1,0,1,-1,1,-1,0,1]

    ind1 = liste_pos[pos-1][0]
    ind2 = liste_pos[pos-1][1]

    board = clean_board(board, liste_pos)

    # Recherche parmis les voisins de la case 'pos', le coup joué
    for i in range(8):
        k2 = ind1 + pos_k[i]
        p2 = ind2 + pos_p[i]

        if k2 < 0 or p2 < 0 or k2 > 7 or p2 > 7:
            continue

        else:

            if board[k2][p2] == 0:
                continue

            elif board[k2][p2] == player:
                continue
            
            # Si la case voisine contient le pion d'un joueur adverse -> regarde si l'origine du coup est atteignable (il peut y avoir plusieurs origines au coup)
            else:
                var = how_far2(board, pos_k[i], pos_p[i], k2, p2, player)
                
                if var == False:
                    continue
                
                # Si l'origine du coup est trouvé -> remplacer les pions du joueur adverse par les pions du joueur courant
                else:
                    var2 = 1
                    k3 = ind1 + pos_k[i] * var2
                    p3 = ind2 + pos_p[i] * var2

                    while ((var[0] == k3) and (var[1] == p3)) == False:
                        board[k3][p3] = player
                        var2 += 1
                        k3 = ind1 + pos_k[i] * var2
                        p3 = ind2 + pos_p[i] * var2

    board[ind1][ind2] = player
    return board

# Permet de netoyer le plateau de jeu des anciens coups possibles
def clean_board(board : 'list[list[int]]', liste_pos : 'list[tuple]') -> 'list[list[int]]':

    for p in liste_pos:
        ind1 = p[0]
        ind2 = p[1]
        board[ind1][ind2] = 0
    
    return board

# Permet de retrouver la position de l'origine du coup joué
def how_far2(board : 'list[list[int]]', ind_k : 'int', ind_p : 'int', k : 'int', p : 'int', player : 'int') -> 'list[int] or False':
    var1 = True
    var2 = 0

    # Recherche dans l'axe de la case voisine les conditions du coup d'origine (similaires à celles d'un coup jouable)
    while var1 == True:
        var2 += 1
        k2 = k + ind_k * var2
        p2 = p + ind_p * var2

        if k2 < 0 or p2 < 0 or k2 > 7 or p2 > 7:
            break
        
        elif (board[k2][p2] == 0):
            break

        elif (board[k2][p2] == player):
            return [k2, p2]

    return False

# Permet de déterminer si une partie est terminée ou non
def end(board : 'list[list[int]]', player : 'int') -> 'int or False':
    list_player = [1, 2]
    k = list_player.index(player)
    next_board = next_pos(board, player)
    
    # Test si aucun des 2 prochains coups n'est jouable
    if next_board == board:
        next_board2 = next_pos(next_board, list_player[k - 1])

        if next_board2 == board:
            return winner(board)
        
        else:
            return False
        
    else:
        return False

# Permet de déterminer le gagnant d'un partie
def winner(board) -> 'int':
    nb1, nb2 = 0, 0

    # Compte le nombre de pion par joueur
    for k in board:

        for p in k:

            if p == 1:
                nb1 += 1
            
            elif p == 2:
                nb2 += 1
            
            else:
                continue
    
    # Compare le nombre de joueur
    if nb1 == nb2:
        return 0
    
    elif nb1 > nb2:
        return 1
    
    else:
        return 2