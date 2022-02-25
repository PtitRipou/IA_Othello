# Affichage du plateau d'Othello

#Retourne la liste des positions initiales du plateau de jeu
def init_othello():
    liste_pos=[]
    for k in range(8):
        liste_pos.append([0,0,0,0,0,0,0,0])
    liste_pos[3][3], liste_pos[4][4] = 1, 1
    liste_pos[3][4], liste_pos[4][3] = 2, 2
    return liste_pos