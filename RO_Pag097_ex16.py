# RO_Pag097_ex16.py
from math import *

#16. El número de pulsaciones que debe tener una persona por cada 10 segundos de
#ejercicio aeróbico se calcula con la fórmula:
#Género femenino (1): número de pulsaciones = (220 - edad en años)/10
#Género masculino (2): número de pulsaciones = (210 - edad en años)/10
#Lea la edad y el género y muestre el número de pulsaciones.

e = float(input("Edat :"))
g = int(input("Genere"))

if g > 2 :
    print("error")
elif g == 1 :
    numero_de_pulsacions = (220 - e) / 10
    print(numero_de_pulsacions)
else :
    numero_de_pulsacions = (210 - e) / 10
    print(numero_de_pulsacions)

