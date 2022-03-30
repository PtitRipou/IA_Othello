# -*- coding: utf-8 -*-
# Fonction de manipulation du plateau d'Othello

# Retourne la liste des positions initiales du plateau de jeu -> 0 = case vide | 1 = player 1 | 2 = player 2
def init_othello() -> 'list[list[int]]': 
    liste_pos=[[0 for k in range(8)] for p in range(8)]

    liste_pos[3][3], liste_pos[4][4] = 2, 2
    liste_pos[3][4], liste_pos[4][3] = 1, 1
    return liste_pos

# Retourne la liste des positions jouable lors de l'affichage du plateau de jeu (l'option 1 permet de retourner la liste sans afficher le plateau)
def display_othello(board: 'list[list[int]]', opt : 'int') -> 'list[tuple]':
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
            
            # si var = 3 alors c'est un position jouable
            elif var == 3:
                all_string += str(nbvar) + "|"
                liste_pos.append((i, p))
                nbvar += 1
    
        k += 1
        all_string += "\n"
    
    if opt == 0:
        print(all_string)

    return liste_pos

# Retourne un plateau de jeu en associant à chaque case la valeur de son poids
def val_board() -> 'list[list[int]]':
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
                    board[a][b] = val_list[a][-(b % 4) - 1]
            
            else:
                if b <= 3:
                    board[a][b] = val_list[-(a % 4) - 1][b]
                
                else:
                    board[a][b] = val_list[-(a % 4) - 1][-(b % 4) - 1]

    return board

# À la manière de val_board(), retourne un plateau avec pour chaque case, la valeur du poids en fonction de sa position par rapport au coin
def dist_corner() -> 'list[list[int]]':
    board = [[1 for k in range(8)] for p in range (8)]
    val_list1 = [40, 3, 20, 10]
    val_list2 = [3, 0, 15, 5]
    val_list3 = [20, 15, 20, 5]
    val_list4 = [10, 5, 5, 5]
    val_list = [val_list1, val_list2, val_list3, val_list4]

    for a in range(8):

        for b in range(8):

            if a <= 3:
                if b <= 3:
                    board[a][b] = val_list[a][b]
                else:
                    board[a][b] = val_list[a][-(b % 4) - 1]
            
            else:
                if b <= 3:
                    board[a][b] = val_list[-(a % 4) - 1][b]
                
                else:
                    board[a][b] = val_list[-(a % 4) - 1][-(b % 4) - 1]

    return board