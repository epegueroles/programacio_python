# RO_Pag146_ex3_quantitat_termes.py
from math import *
#3. Determine la cantidad de términos que deben sumarse de la serie 1^2+ 2^2+ 33+ 4^4+ ...
#para que el valor de la suma sea mayor a un número x ingresado al inicio.

x = float(input("numero :"))
n = 1
suma = 1
quantitat_vegades = 1

while suma < x :
    suma = pow(n,n)
    n = n + 1
    quantitat_vegades = n + 1
    print(suma, "suma de cada nombre")
    print(quantitat_vegades,"vegades")