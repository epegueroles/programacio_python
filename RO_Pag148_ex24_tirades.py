# RO_Pag148_ex24_tirades.py
from math import *
from random import *

n = int(input("Núumero de tirades :"))
x = 0
diners = 0
tirada = 0
while x < n :
    x = x + 1
    tirada = randint(1,6)
    if tirada == 6 :
        diners = diners + 5
    elif tirada == 1 :
        diners = diners + 1
    else :
        diners = diners - 2
print(f"En les {n} tirades, has guanyat o perdut {diners}$")