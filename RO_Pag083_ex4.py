# RO_Pag83_ex4.py
from math import *

a = int(input("numero de tres xifres ="))

b = a // 10
b2 = b % 10
c = a // 100
d = a % 10

num_canviat = (d * 100) + (b2 * 10) + c

print("numero canviat és",num_canviat)