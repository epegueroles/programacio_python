# RO_Pag146_ex4_mcd.py
from math import *
#4.- Dado dos números enteros a, b, determine su máximo común divisor m. 

a = int(input("a = "))
b = int(input("b = "))
mcd = 0
n =  1
d = 0
c = 0
while n != b:
    n = n + 1
    d = a / n
    c = b / n
    if d %1 == 0 and c % 1 == 0:
        mcd = n

print(mcd)