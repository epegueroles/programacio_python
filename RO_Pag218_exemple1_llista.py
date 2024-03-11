# RO_Pag218_exemple1_llista.py
from math import *

n = int(input("Quantitat de numeros: "))
v = []
for i in range(n):
    x = int(input("Ingressa el seguent valor: "))
    v = v + [x]
print("Llista inicial : ", v)
u = []
for e in v:
    if e not in u:
        u = u + [e]
print("Llista difinitiva : ", u)