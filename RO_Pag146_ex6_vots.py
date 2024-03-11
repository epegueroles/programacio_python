# RO_Pag146_ex6_vots.py
from math import *
#6.- Lea los votos de n personas. Cada voto es un número 1, 2, o 3 correspondiente a tres
#candidatos. Si el dato es 0 es un voto en blanco. Si es otro número es un voto nulo.
#Determine el total de votos de cada candidato y el total de votos blancos y nulos

n = int(input("quantitat de vots ="))
vot = 1
g1 = 0
g2 = 0
g3 = 0

while vot < n:
    opcio = int(input("a qui vols votar? : "))
    vot = vot + 1
    if opcio == 1 :
        g1 = g1 + 1
print(g1)
