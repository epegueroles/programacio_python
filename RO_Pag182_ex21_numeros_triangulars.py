# RO_Pag182_ex21_numeros_triangulars.py
from math import*

def triangular_for(n):
    fx = 0
    for i in range(1,n+1):
        fx = fx + i
        print(f"n = {i} i f(x) = {fx}")
    return fx

def suma_f(n):
    fx = 0
    suma = 0
    for i in range(1,n+1):
        fx = fx + i
        suma += fx
        print(f"suma = {suma}")
    return suma_f
print("MENU")
print("1 Nombres triangulars")
print("2 Suma nombres triangulars")
r = int(input("Tria el que vols calcular: "))
if r == 1:
    n = int(input("n = "))
    triangular_for(n)
elif r == 2:
    n = int(input("n = "))
    suma_f(n)
else :
    print("error")