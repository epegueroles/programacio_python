# RO_Pag147_ex22_granotes.py
from math import *
from random import *

meta = 20
inici = 0
tirades = [0, 0.5, 1, -1]
numero_tirades = 0
g1 = 0
g2 = 0
g3 = 0
posicio = 0
while posicio < meta :
    g1 = choice(tirades) + g1
    g2 = choice(tirades) + g2
    g3 = choice(tirades) + g3
    numero_tirades = numero_tirades + 1
    posicio1 = g1
    posicio2 = g2
    posicio3 = g3
    
    if g1 > g2 and g1 > g3 :
        posicio = posicio1
        print(posicio1,"g1")
    elif g2 > g1 and g2 > g3 :
        posicio = posicio2
        print(posicio2,"g2")
    elif g3 > g1 and g3 > g2 :
        posicio = posicio3
        print(posicio3,"g3")
    elif g1 == g2 and g1 == g3:
        posicio = posicio1
        print("Empat")
    elif g1 == g2 or g1 == g3:
        posicio = posicio1
        print(posicio1,"g1")
    
if posicio1 > posicio2 and posicio1 > posicio3 :
    print("Ha guanyat la granota 1")
elif posicio2 > posicio1 and posicio2 > posicio3 :
    print("Ha guanyat la granota 2")
elif posicio3 > posicio1 and posicio3 > posicio2 :
    print("Ha guanyat la granota 3")
elif posicio1 == posicio2 and posicio1 == posicio3:
    print("Ha guanyat la granota 1")
elif posicio1 == posicio2 or posicio1 == posicio3:
    print("Ha guanyat la granota 1")
    
print(f"Ha fet {numero_tirades} salts :)")
    
        