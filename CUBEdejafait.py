### Groupe 0

## Importation des bibliothèques

import math as m
import time as t
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

## Fonctions utiles

def vitesse_collision(VA,VB,mA,mB):
    VA_2 = ((mA- mB)/(mA + mB)*VA + (2*mB)/(mA + mB)*VB)
    VB_2 = ((2*mA)/(mA + mB)*VA + (mB - mA)/(mA + mB)*VB)
    return(VA_2,VB_2)

## Fonction qui compte le nombre de collisions utilisé pour la modélisation

def déplacement(N) :
    "Renvoie les N premiéres decimales de pi"

    mA = 1 # On définit les valeurs des masses des cubes : Cube A = petit cube (masse constante) / Cube B = grand cube (masse choisie)
    mB = 100**(N-1)

    xAG , xAD = 1, 2 # On définit les positions initiales des cubes
    xBG , xBD = 3 , 5

    VA = 0 # On définit les vitesses initiales : Cube A fixe / Cube B vitesse initiale fixée
    VB = -1

    nb_collision = 0 # Compteur de collisions

    while not (0<=VA <= VB) :  # Tant que le gros cube B n'a pas une vitesse supérieur à celle du petit cube A et que ces vitesses sont positives (les cubes s'éloignent), on calcul les positions

        dt = 0.001

        xAG , xAD = xAG + dt*VA , xAD + dt*VA # Les positions des cubes évoluent en fonction de la vitesse de manière infinitésimale
        xBG , xBD = xBG + dt*VB , xBD + dt*VB

        if xAG <= 0 : # Si le cube A rencontre le mur, on revient à la position précédente et on repart dans l'autre sens, + 1 collision

            xAG , xAD = 0 , 1 # On replace le cube à l'origine !! On remarque qu'en replaçant le cube à la mauvaise position le programme est bien plus efficace(par exemple à 0 , 12 on peut aller jusqu'à 8 décimales (le derniere est erronée) !!
            VA = -VA
            nb_collision += 1

        if xAD >= xBG : # Si les cubes se rencontrent, on revient à la position précédente et chaque cube repart dans l'autre sens, les vitesses sont modifiées

            xBG , xBD = xBG - dt*VB , xBD - dt*VB
            xAG , xAD = xAG - dt*VA , xAD - dt*VA

            VA, VB = vitesse_collision(VA,VB,mA,mB)
            nb_collision += 1

    return(nb_collision)

## Fonction qui renvoie les listes de positions des cubes

def pos(mb) : #Meme fonction que pour les décimales de pi mais qui renvoie une listes des coordonées des differents murs
    "Cette fonction renvoie la liste de coordonnées des cubes"
    AG=[]
    AD=[]
    BG=[]
    BD=[]
    L=[]
    mA = 1 # On définit les valeurs des masses des cubes : Cube A = petit cube (masse constante) / Cube B = grand cube (masse choisie)
    mB = mb

    xAG , xAD = 1, 5 # On définit les positions initiales des cubes
    xBG , xBD = 7 , 12

    VA = 0 # On définit les vitesses initiales : Cube A nulle / Cube B vitesse initiale fixée
    VB = -1

    nb_collision = 0 # Compteur de collisions

    while not (0<=VA <= VB) :  # On définit une boucle qui fait marcher le système tant que le cube B ne s'éloigne pas trop

        dt = 0.01

        xAG , xAD = xAG + dt*VA , xAD + dt*VA # Les positions des cubes évoluent en fonction de la vitesse
        xBG , xBD = xBG + dt*VB , xBD + dt*VB

        if xAG <= 0 : # Si le cube A rencontre le mur, on revient à la position précédente et on repart dans l'autre sens, + 1 collision

            xAG , xAD = 0 , 4 # on replace le cube à l'origine
            VA = -VA
            nb_collision += 1

        if xAD >= xBG : # Si les cubes se rencontrent, on revient à la position précedente et chaque cube repart dans l'autre sens, les vitesses sont modifiées

            xBG , xBD = xBG - dt*VB , xBD - dt*VB
            xAG , xAD = xAG - dt*VA , xAD - dt*VA

            VA, VB =  ((mA- mB)/(mA + mB)*VA + (2*mB)/(mA + mB)*VB), ((2*mA)/(mA + mB)*VA + (mB - mA)/(mA + mB)*VB)
            nb_collision += 1

        AG.append(xAG) #Insertion des coordonées des murs
        AD.append(xAD)
        BG.append(xBG)
        BD.append(xBD)

    L.append(AG)
    L.append(AD)
    L.append(BG)
    L.append(BD)
    return L #On renvoie une liste contenant les listes des coordonées

## Modélisation

# Murs

m=100 #Faire varier la masse d'entrée pour différentes situations : 1,100,10000... avec 100 le plus visuel et parlant

X1 = pos(m)[0] #Coordonées petit mur gauche

X2 = pos(m)[1] #Coordonées petit mur droit

X3 = pos(m)[2] #Coordonées grand mur gauche

X4 = pos(m)[3] #Coordonées grand mur droit


#Bug de visualistion pour m>10000

# Abscice constante
Y = [1 for i in range(len(X1))]

fig, ax = plt.subplots()
lines = [ax.plot([], [], style, markersize=100)[0] for style in ['r|','r|','b|','b|']] #On crée les figures des cubes

def init():
    "Création du cadre de la simulation"
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Animation du déplacement des cubes')
    ax.grid(True)
    return lines

def update(frame):
    "Fonction permettant d'actualiser la simulation pour animer les points"

    for i, line in enumerate(lines):#On parcourt indice et liste à la fois (à l'aide de i, line) pour les 4 tracés de murs
        if i == 0 and frame < len(X1): #On traite le cas de la ligne 0, tant qu'on a des valeurs disponibles ( Nombre de frames écoulées inférieur au nombre de valeurs )
            line.set_data([], []) #On efface la ligne
            lines[i].set_data(X1[frame], Y[frame]) #Nouvelles coordonées

        elif i == 1 and frame < len(X2):#De meme pour les autres murs

            line.set_data([], [])
            lines[i].set_data(X2[frame], Y[frame])

        elif i == 2 and frame < len(X3):

            line.set_data([], [])
            lines[i].set_data(X3[frame], Y[frame])

        elif i == 3 and frame < len(X4):
            line.set_data([], [])
            lines[i].set_data(X4[frame], Y[frame])

    return lines

ani = FuncAnimation(fig, update, frames=max(len(x) for x in [X1, X2, X3, X4]), init_func=init, blit=True, interval=6) #permet l'animation, avec un intervalle de temps entre les points plus ou moins grand
plt.show()