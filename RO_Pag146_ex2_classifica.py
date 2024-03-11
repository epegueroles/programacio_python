# RO_Pag146_ex2_classifica.py
from math import *
#2.- Clasifique los pesos de los n objetos de una bodega en tres grupos: menor a 10 Kg.,
#entre 10 y 20 Kg., mas de 20 Kg. Los datos ingresan uno a la vez en un ciclo.

n = int(input("numero objectes ="))
x = 0
while x != n :
    pes =  int(input("Pes del paquet en kg ="))
    x = x + 1
    if pes < 10:
        grup1 = pes
        print(pes,"kg  Pertany al grup 1")
    elif pes < 20:
        grup2 = pes
        print(pes,"kg  Pertany al grup 2")
    else :
        print(pes,"kg  Pertany al grup 1")