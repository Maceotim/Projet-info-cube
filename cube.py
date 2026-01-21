import numpy as np
import matplotlib.pyplot as plt

#Conservation de l'énergie :
#1/2 * m1 * v1**2 + 1/2 * m2 * v2**2 = cste

#Conservation du moment :
# m1v1 + m2v2 = cste

class Cube :

    def __init__(self, masse, vitesse, abscisse):
        self.masse = masse
        self.vitesse = vitesse
        self.abscisse = abscisse


cube1 = Cube(1, 0, 10)
cube2 = Cube(2, -1, 200)

def nouvelles_vitesses(va, vb) :
    va2 = (cube1.masse*va - cube2.masse*(va - 2*vb))/(cube1.masse + cube2.masse)
    vb2 = va + va2 - vb
    return (va2, vb2)
