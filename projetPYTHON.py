
'''
Author : Athos Cruchet
Date : 26.01.2024
Description : 2048 affichage
'''
import random
from tkinter import *
import tkinter.messagebox

#variables


#création de la fenêtre
window = Tk()
window_width = 900
window_height = 600
# taille de la fenêtre
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# fenêtre centrée
x_left = int(screen_width/2 - window_width/2)
y_top = int(screen_height/2 - window_height/2)
window.title("2048")
# move window center
window.geometry(f"{window_width}x{window_height}+{x_left}+{y_top}")

# liste des nombres
numbers = [[2, 4, 8, 16, 32],
           [64, 128, 256, 512, 1024],
           [2048, 4096, 8192, 16384,0]]
'''
# exemple partie commencée
numbers = [[2, 0, 0, 0, 0],
           [0, 0, 0, 0, 4],
           [0, 0, 0, 0]]
'''

labels = [[None, None, None, None, None],
          [None, None, None, None, None],
          [None, None, None, None, None]]

#dictionnaire des couleurs
colors = {
    "text": "#BFBFB8",
    "ground": "#4C594F",
    0: "#AAAAA3",
    2: "#1F2A24",
    4: "#27322C",
    8: "#313C36",
    16: "#35403A",
    32: "#404B45",
    64: "#404B45",
    128: "#46514B",
    256: "#4C5851",
    512: "#57635C",
    1024: "#626E67",
    2048: "#7A867F",
    4096: "#94A099",
    8192: "#B5C1BA"
}
# FUNCTIONS
# Function that displays the numbers and colors
def display():
    for li in range(len(numbers)):
        for col in range(len(numbers[li])):
            # placement du label dans la fenêtre par ses coordonnées en pixels
            labels[li][col].config(text=numbers[li][col], bg=colors[0], fg="white")

# WINDOW'S DISPLAY
frame_background = Frame(window, bg="#70726E")
frame_background.pack(expand=TRUE, fill=BOTH)
# Title
label_title = Label(window, text="2048", font=("Arial", 50), bg="#70726e", fg="white")
label_title.place(x=100, y=40)
# Label score
label_score = Label(window, text="SCORE : 0  ", borderwidth=1, relief="solid", font=35, background="#AAAAA3")
label_score.place(x=500, y=94)

# Background of the grid
grid_background = Label(window, text="", bg="#70726e", height=23, width=72, borderwidth=2, relief="solid")
grid_background.place(x=91, y=118)
# Reset Button
new_game = Button(grid_background, text="Nouvelle partie", background="#AAAAA3", fg="black")
new_game.place(x=9, y=315)

#tutoriel
def tuto():
    fenetre_tuto = Tk()
    fenetre_tuto.wm_withdraw()
    tkinter.messagebox.showinfo(title="tutoriel", message="Le but du jeu est de faire glisser des tuiles sur la"
                                                          " grille, pour combiner les tuiles de mêmes valeurs et créer"
                                                          " ainsi une tuile portant le nombre 2048. Le joueur peut"
                                                          " toutefois continuer à jouer après cet objectif atteint "
                                                          "pour faire le meilleur score possible!.")# font=20)
    fenetre_tuto.destroy()
    return None

# bouton tutoriel
tuto = Button(grid_background, text="?", font=25,background="#AAAAA3", command = tuto)
tuto.place(x=478, y=310)


# list of labels
labels = [[None, None, None, None, None],
          [None, None, None, None, None],
          [None, None, None, None, None],]

width = 100  # horizontal distance between labels
# Labels creation
for li in range(len(numbers)):
    for col in range(len(numbers[li])):
        # Creates the Lables without displaying them
        labels[li][col] = Label(window, text="", width=8, height=4, borderwidth=2, relief="solid", font=("Arial", 15))
        # places the grid with precise positioning
        labels[li][col].place(x=100 + width * col, y=125+width*li)
display()

# Généré 2-4 aléatoirement avec 80% de chance que ce soit un 2
def spawn():
    if random.random() >= 0.8:
        return 2
    else:
        return 4

def newgame():
    global labels
    del labels


def tasse_5(a, b, c, d, e, bscore):
    global score
    nmove = 0
    # ici le code va manipuler a, b, c, d et e
    # les zéros sont poussés à droite
    if (d == 0 and e > 0):
        d, e = e, 0  # spécialité de Python pour inverser 2 variables
        nmove += 1
    if (c == 0 and d > 0):
        c, d, e = d, e, 0
        nmove += 1
    if (b == 0 and c > 0):
        b, c, d, e = c, d, e, 0
        nmove += 1
    if (a == 0 and b > 0):
        a, b, c, d, e = b, c, d, e, 0
        nmove += 1
    # on fusionne deux par 2 les tuiles identiques
    if (a == b and a > 0):
        a, b, c, d, e = a + b, c, d, e, 0
        if bscore:
            score += a
        nmove += 1
    if (b == c and b > 0):
        b, c, d, e = b + c, d, e, 0
        if bscore:
            score += b
        nmove += 1
    if (c == d and c > 0):
        c, d, e = c + d, e, 0
        if bscore:
            score += c
        nmove += 1
    if (d == e and d > 0):
        d, e = d + e, 0
        if bscore:
            score += d
        nmove += 1
    # ici on retourne les six valeurs en un tableau
    temp = [a, b, c, d, e, nmove]  # tableau temporaire de fin
    return temp



window.mainloop()