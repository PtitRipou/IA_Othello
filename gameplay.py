# -*- coding: utf-8 -*-
#Implémentation des instrunctions de jeu

import othello_board as ob
import copy

#Permet de déterminer les positions suivantes possible pour une configuration de plateau
def next_pos(board : 'list[list[int]]', player : 'str'):
    next_board = copy.deepcopy(board)
    player_int = 0

    if player == "player1":
        player_int = 1

    elif player == "player2":
        player_int = 2

    else:
        print("Error : Not a valid player !")
    
    for k in range(8):
        for p in range(8):

            if board[k][p] == player_int :
                list_play = list_possible_play(board, k, p, player_int)
                if list_play != []:
                    for i in range(len(list_play)):
                        next_board[list_play[i][0]][list_play[i][1]] = 3

    return next_board

#Détermine si le pion en p,k permet de jouer un coup (analyse des pions voisins)
def list_possible_play(board, k, p, player):
    pos_k = [-1,-1,-1,0,0,1,1,1]
    pos_p = [-1,0,1,-1,1,-1,0,1]
    list_play = []

    for i in range(8):
        k2 = k + pos_k[i]
        p2 = p + pos_p[i]

        if k2 < 0 or p2 < 0 or k2 > 7 or p2 > 7:
            continue

        else:

            if board[k2][p2] == 0:
                continue

            elif board[k2][p2] == player:
                continue

            else:
                var = how_far(board, pos_k[i], pos_p[i], k2, p2, player)
                
                if var == False:
                    continue

                else:
                    list_play.append(var)

    return list_play

#Permet de savoir, lorsqu'un pion est voisin d'un pion adverse, si un coup est jouable
def how_far(board, ind_k, ind_p, k, p, player):
    var1 = True
    var2 = 0

    while var1 == True:
        var2 += 1
        k2 = k + ind_k * var2
        p2 = p + ind_p * var2

        if k2 < 0 or p2 < 0 or k2 > 7 or p2 > 7:
            break

        elif board[k2][p2] == player:
            break

        elif board[k2][p2] == 0:
            return [k2, p2]

    return False

board = ob.init_othello()
next_board = next_pos(board, 'player1')
ob.display_othello(next_board)