# RO_Pag097_ex15.py
from math import *

# 15. Un código de tres cifras debe cumplir la siguiente regla para que sea vàlido:
#La tercera
#cifra debe ser igual al mòdulo 10 del producto de las dos primeras cifras. Escriba un
#programa que lea un código y verifique si cumple la regla anterior. Muestre un mensaje
#correspondiente.
#Ejemplo. 384 es un código vàlido pues el módulo de 3x8 en 10 es igual a 4

n = float(input("Numero :"))

(n1,m) = divmod(n,100)
(n2,n3) = divmod(m,10)
print(n1)
print(n2)
print(n3)


if (n1 * n2) % 10 == n3 :
    print("El codi es valid")
else :
    print("El codi no es valid")