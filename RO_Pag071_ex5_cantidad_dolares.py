# RO_Pag71_ex5_cantidad_dolares.py
from math import *

p = 300 *12
n = 15
x = 0.04
a = p * ((pow(1 + x, n) - 1) / x )
print("apartat a) =",a)


a = 200000
n = 20
x = 0.04
p = (a / ((pow(1 + x, n) - 1) / x ))/12
print("apartat b) =",p)


a = 250000
x = 0.04
p = 400 * 12
n = (log(x * (a / p) + 1)/(log(1+x)))
print("apartat c) =",n)