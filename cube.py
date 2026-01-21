import numpy as np
import matplotlib.pyplot as plt

#Conservation de l'énergie :
#1/2 * m1 * v1**2 + 1/2 * m2 * v2**2 = cste

#Conservation du moment :
# m1v1 + m2v2 = cste

class Cube:

    def __init__(self, masse, vitesse, abscisse):
        self.masse = masse
        self.vitesse = vitesse
        self.abscisse = abscisse


cube1 = Cube(1, 0, 10)
cube2 = Cube(2, -1, 200)

energie = 0.5*(cube1.masse*cube1.vitesse**2 + cube2.masse*cube2.vitesse**2)

print(np.random.randint(10))