# RO_Pag150_ex36_sumatori.py
from math import*

n = int(input("Introdueix n  "))
m = int(input("Introdueix m  "))
som = 0
b = 0
if n < m:
    aux = n
    n = m
    m = n

for a in range(1, n + 1):
    if b < m+1:
        b += 1
    som += pow(a,2) + pow(b,2) + a * b



print(som)