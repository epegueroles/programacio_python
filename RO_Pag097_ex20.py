# RO_Pag097_ex20.py
from math import *

#20. Dadas las dimensiones de un bloque rectangular, calcule y muestre el área de la cara
#de mayor dimensión.

l = float(input("llargada :"))
a = float(input("amplada :"))
h = float(input("haltura :"))


a1 = h * a
print(a1,"area 1")
a2 = h * l
print(a2,"area 2")
a3 = l * a
print(a3,"area 3")

if a1 > a2 and a1 > a3 :
    print("L'area mes gran es :",a1)
elif a2 > a1 and a2 > a3 :
    print("L'area mes gran es :",a2)
elif a3 > a1 and a3 > a2 :
    print("L'area mes gran es :",a3)
elif a1 == a2 and a1 == a3 :
    print("Totes son iguals :",a1,a2,a3)
else :
    print("error")
