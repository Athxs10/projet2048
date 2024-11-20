from tkinter import *
import tkinter.font
import random
import copy
from tkinter import messagebox
from tkinter import *
from tkinter import messagebox
import tkinter.font
import random


# Variable
first2048 = 1
best_score = 0


# Dictionnaire de couleurs
colorsLib = {
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


# Tableau 2 dimensions avec des mots (3x5)
words = [[2, 4, 8, 16, 32],
         [64, 128, 256, 512, 512],
         [1024, 1024, 4096, 0, 0]]


# Tableau 2 dimensions avec des vides qui deviendront des labels.
labels = [[None, None, None, None, None],
          [None, None, None, None, None],
          [None, None, None, None, None]]

width1 = 90  # espacement horizontal en pixels des étiquettes (remarque la taille des labels est en caractères)
height1 = 60  # espacement vertical en pixels des étiquettes


# Construction de la fenêtre :
window = Tk()
window.geometry("630x360")
window.title('2048')
window.configure(bg=colorsLib["ground"])

#Labels
labelTitle = Label(window, text="2048", font=("Comic Sans MS", 52), bg=colorsLib["ground"], fg=colorsLib["text"])
labelTitle.place(x=20, y= -15)

labelUTitle = Label(window, text="Obtenez le nombre 2048", font=("Comic Sans MS", 16), bg=colorsLib["ground"], fg=colorsLib["text"])
labelUTitle.place(x=23, y= 70)

labelGrounde = Label(window, text="",bg=colorsLib["text"], width=63, height=12, relief="solid", borderwidth=2)
labelGrounde.place(x=92, y=142)



# Création des labels (d'abord on les définit avec =, puis on les place dans la fenêtre avec .place(x,y)
for line in range(len(words)):
    for col in range(len(words[line])):
        # Construction de chaque label sans le placer
        labels[line][col] = tkinter.Label(text="", width=6, height=2, borderwidth=2, relief="solid", font=("Arial", 15))
        # Placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][col].place(x=100 + width1 * col, y=150 + height1 * line)




# Généré 2-4 aléatoirement avec 80% de chance que ce soit un 2
def spawn():
    if random.random() >= 0.8:
        return 4
    else:
        return 2


# Remplace les nombres générés précédemment
def generate():
    candidate = []
    for line in range(len(words)):
        for col in range(len(words[line])):
            if words[line][col] == 0:
                candidate.append([line, col])

    line, col = random.choice(candidate)
    words[line][col] = spawn()



    display()


# Définition du bouton New_Game
def new_game():
    global words, score, best_score
    words = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    score = 0
    generate()
    generate()
    display()
    best_score = max(best_score, score)


# Affiche les couleurs automatiquement
def display():
    global best_score
    for line in range(len(words)):
        for col in range(len(words[line])):
            if words[line][col] == 0:
                labels[line][col].config(text="", bg=colorsLib[0])
            else:
                labels[line][col].config(text=words[line][col], bg=colorsLib[words[line][col]])



score = 0
display()


# Message lorsqu'on perd
def perdre():
    global words, score, best_score
    partie_perdue = 0
    words_2 = copy.deepcopy(words)

    # Haut
    for col in range(len(words[0])):
        [words_2[0][col], words_2[1][col], words_2[2][col], a] = tasse_3(words_2[0][col], words_2[1][col],
                                                                         words_2[2][col], False)
        partie_perdue += a

        # Gauche
        for line in range(len(words)):
            [words_2[line][0], words_2[line][1], words_2[line][2], words_2[line][3], words_2[line][4], a] = tasse_5(
                words_2[line][0], words_2[line][1], words_2[line][2], words_2[line][3], words_2[line][4], False)
            partie_perdue += a

    # Droite
    for line in range(len(words)):
        [words_2[line][4], words_2[line][3], words_2[line][2], words_2[line][1], words_2[line][0], a] = tasse_5(
            words_2[line][4], words_2[line][3], words_2[line][2], words_2[line][1], words_2[line][0], False)
        partie_perdue += a





    if partie_perdue == 0:
        rep = messagebox.askretrycancel("askretrycancel", "Voulez-vous recommencer (retry) ou quitter (cancel)?")

        if rep:
            new_game()
        else:
            quit()
    else:
        best_score = max(best_score, score)
        display()


# Définition du message victoire
def victory():
    global first2048
    for line in range(len(words)):
        for col in range(len(words[line])):
            if first2048 == 1:
                if words[line][col] == 2048:
                    messagebox.showinfo("2048 !", "Vous avez fait 2048 !")
                    first2048 = 0
                if words[line][col] == 8192:
                    messagebox.showinfo("Victory", "Vous avez gagné !")


# Définir les mouvements du tassement
def tasse_left(event):
    cal = 0
    for line in range(len(words)):
        [words[line][0], words[line][1], words[line][2], words[line][3], words[line][4], n] = tasse_5(
            words[line][0], words[line][1], words[line][2], words[line][3], words[line][4], True)
        cal += n
    if cal > 0:
        generate()
    victory()
    perdre()
    display()


def tasse_right(event):
    cal = 0
    for line in range(len(words)):
        [words[line][4], words[line][3], words[line][2], words[line][1], words[line][0], n] = tasse_5(
            words[line][4], words[line][3], words[line][2], words[line][1], words[line][0], True)
        cal += n
    if cal > 0:
        generate()
    victory()
    perdre()
    display()


def tasse_up(event):
    cal = 0
    for col in range(len(words[0])):
        [words[0][col], words[1][col], words[2][col], n] = tasse_3(words[0][col], words[1][col], words[2][col], True)
        cal += n
    if cal > 0:
        generate()
    victory()
    perdre()
    display()


def tasse_down(event):
    cal = 0
    for col in range(len(words[0])):
        [words[2][col], words[1][col], words[0][col], n] = tasse_3(words[2][col], words[1][col], words[0][col], True)
        cal += n
    if cal > 0:
        generate()
    victory()
    perdre()
    display()


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


def tasse_3(a, b, c, bscore):
    global score
    nmove = 0
    # ici le code va manipuler a, b et c
    # les zéros sont poussés à droite
    if (b == 0 and c > 0):
        b, c = c, 0  # spécialité de Python pour inverser 2 variables
        nmove += 1
    if (a == 0 and b > 0):
        a, b, c = b, c, 0
        nmove += 1
    # on fusionne deux par 2 les tuiles identiques
    if (a == b and a > 0):
        a, b, c = a + b, c, 0
        if bscore:
            score += a
        nmove += 1
    if (b == c and b > 0):
        b, c = b + c, 0
        if bscore:
            score += b
        nmove += 1
    # ici on retourne les quatre valeurs en un tableau
    temp = [a, b, c, nmove]  # tableau temporaire de fin
    return temp


# Attraper les touches pour les mouvements
window.bind("<d>", tasse_right)
window.bind("<a>", tasse_left)
window.bind("<s>", tasse_down)
window.bind("<w>", tasse_up)

window.bind("<D>", tasse_right)
window.bind("<A>", tasse_left)
window.bind("<S>", tasse_down)
window.bind("<W>", tasse_up)

window.bind("<Right>", tasse_right)
window.bind("<Left>", tasse_left)
window.bind("<Down>", tasse_down)
window.bind("<Up>", tasse_up)

button_nouveau = Button(command=new_game, text="New Game", background="#CAD2D7")
button_nouveau.place(x=197, y=40)

window.mainloop()