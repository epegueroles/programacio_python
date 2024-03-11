# RO_Pag097_ex18.py
from math import *

#18. Otro reporte de salud muestra una tabla diferente del índice de masa corporal IMC de
#una persona que se calcula con la fórmula IMC=P/T2en donde P es el peso en Kg. y T es
#la talla en metros.

p = float(input("pes :"))
t = float(input("talla :"))

imc = p/pow(t,2)
print("imc = ",imc)
if imc < 20 :
    print("desnutrit")
elif imc < 25 :
    print("normal")
elif imc < 30 :
    print("sobrepeso")
elif imc < 35 :
    print("Obessitat grau 1")
elif imc < 40 :
    print("Obessitat grau 2")
else :
    print("Obessitat grau 3")