# -*- coding: utf-8 -*-
# Affichage du plateau d'Othello

#Retourne la liste des positions initiales du plateau de jeu
def init_othello():
    liste_pos=[]

    for k in range(8):
        liste_pos.append([0,0,0,0,0,0,0,0])

    liste_pos[3][3], liste_pos[4][4] = 2, 2
    liste_pos[3][4], liste_pos[4][3] = 1, 1
    return liste_pos

# Permets d'afficher le plateau de jeu
def display_othello(board: 'list[list[int]]'):
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
    
    print(all_string)
    return liste_pos