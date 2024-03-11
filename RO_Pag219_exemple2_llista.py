# RO_Pag219_exemple2_llista.py
from math import *

def norep(v):
    u = []
    for e in(v):
        if e not in u:
            u = u + [e]
    return u

            
n = int(input("Quantitat de numeros: "))
v = []
for i in range(0,n):
    x = int(input("Ingressa el seguent valor: "))
    v = v + [x]
print("Llista inicial: ", v)
print("Llista difinitiva: ", norep(v))