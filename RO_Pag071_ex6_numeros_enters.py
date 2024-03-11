# RO_Pag71_ex6_numeros_enters.py

from math import *

x = int(input("numero enter 1 ="))
y = int(input("numero enter 2 ="))

# Obtenga los resultados de las restas
resta_1 = 1000 - x # numero enter 1
resta_2 = 1000 - y # numero enter 2

# Sume los resultados de las restas
suma_resultats = resta_1 + resta_2

# Reste de 1000 el resultado de la suma
mil_menys_resultats = 1000 - suma_resultats

# Multiplique este resultado por 1000
resultat_mutiplicacio = mil_menys_resultats * 1000

# Multiplique los resultados de las restas iniciales
mutiplicacio_entre_ells = resta_1 * resta_2

# La suma de los dos últimos resultados es el producto deseado
total = resultat_mutiplicacio + mutiplicacio_entre_ells

print(total)