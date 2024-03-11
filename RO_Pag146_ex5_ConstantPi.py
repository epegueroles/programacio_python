# RO_Pag146_ex5_ConstantPi.py
from math import *
#5. Calcule un valor aproximado para la constante π usando la siguiente expresión:

n = int(input("quantitat de termes ="))
x = 1
pi = 0
i = 1
while i < n :
    if i % 2 == 0 :
        k = (1 / x) * (-1)
    else :
        k = (1 / x)
    x = x + 2
    pi = pi + k
    i = i + 1
    print("pi = ",pi)

pi = 4 * pi

print("pi = ",pi)
print("gracies per l'espera :)")