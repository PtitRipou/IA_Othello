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
    k = 1
    nbvar = 1

    for i in board:
        all_string += str(k) + " |"

        for p in i:

            if p == 0:
                all_string += "_|"
            
            elif p == 1:
                all_string += "○|"
            
            elif p == 2:
                all_string += "●|"
            
            elif p == 3:
                all_string += str(nbvar) + "|"
                nbvar += 1
    
        k += 1
        all_string += "\n"
    
    print(all_string)


board = init_othello()
display_othello(board)