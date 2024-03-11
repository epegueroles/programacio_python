# RO_Pag146_ex1_num_paquets.py
# Ex 1
#1.- Calcule el promedio, el menor valor y el mayor valor de los pesos de n paquetes en una
#bodega. Estos datos ingresan uno a la vez dentro de un ciclo. n es un dato ingresado al
#inicio.
from math import *
pes1 = int(input("Pes del paquet 1 = "))
n = int(input("numero paquets="))
pes_max = pes1
pes_min = pes1
suma = pes1
x = 1
while x != n :
    pes = int(input(f"pes del paquet en kg ="))
    x = x + 1
    suma = pes + suma
    if pes > pes_max :
        pes_max = pes
    elif pes < pes_min :
        pes_min = pes
pes_mitja = suma / n

print("El pes mitja es :",pes_mitja ,"kg")
print("El pes minim dels paquets es :", pes_min ,"kg")
print("El pes maxim dels paquets es :", pes_max ,"kg")