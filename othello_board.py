# -*- coding: utf-8 -*-
# Affichage du plateau d'Othello

# Retourne la liste des positions initiales du plateau de jeu
def init_othello():
    liste_pos=[]

    for k in range(8):
        liste_pos.append([0,0,0,0,0,0,0,0])

    liste_pos[3][3], liste_pos[4][4] = 2, 2
    liste_pos[3][4], liste_pos[4][3] = 1, 1
    return liste_pos

# Permets d'afficher le plateau de jeu
def display_othello(board: 'list[list[int]]', opt : 'int'):
    all_string = "   a b c d e f g h\n"
    liste_pos = []
    k = 1
    nbvar = 1

    for i in range(8):
        all_string += str(k) + " |"

        for p in range(8):
            var = board[i][p]

            if var == 0:
                all_string += " |"
            
            elif var == 1:
                all_string += "○|"
            
            elif var == 2:
                all_string += "●|"
            
            elif var == 3:
                all_string += str(nbvar) + "|"
                liste_pos.append((i, p))
                nbvar += 1
    
        k += 1
        all_string += "\n"
    
    if opt == 0:
        print(all_string)

    return liste_pos

#Permet d'associer aux cases du plateau de jeu des valeurs
def val_board():
    board = [[1 for k in range(8)] for p in range (8)]
    val_list1 = [40, 3, 15, 10]
    val_list2 = [3, 0, 9, 12]
    val_list3 = [15, 9, 11, 15]
    val_list4 = [10, 12, 15, 18]
    val_list = [val_list1, val_list2, val_list3, val_list4]

    for a in range(8):
        for b in range(8):

            if a <= 3:
                if b <= 3:
                    board[a][b] = val_list[a][b]
                else:
                    board[a][b] = val_list[a][-(b%4)-1]
            
            else:
                if b <= 3:
                    board[a][b] = val_list[-(a%4)-1][b]
                
                else:
                    board[a][b] = val_list[-(a%4)-1][-(b%4)-1]

    return board