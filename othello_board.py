# Affichage du plateau d'Othello

#Retourne la liste des positions initiales du plateau de jeu
def init_othello():
    liste_pos=[]
    for k in range(8):
        liste_pos.append([0,0,0,0,0,0,0,0])
    liste_pos[3][3], liste_pos[4][4] = 2, 2
    liste_pos[3][4], liste_pos[4][3] = 1, 1
    return liste_pos

# Permets la gestion de l'affichage
def display_othello(board: 'list[list[int]]'):
    print("   a  b  c  d  e  f  g  h")
    k = 1
    for i in board:
        print(k,i)
        k+=1

board = init_othello()
display_othello(board)