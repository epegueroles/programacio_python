# RO_Pag95_ex1.py
from math import *

radi = float(input("radi ="))
altura = float(input("altura ="))

if altura > radi :
    volum = 3.1416 * radi * radi * altura
    print("volum =", volum)
else :
    area = (2 * 3.1416 * radi * radi) + (2 * radi * 3.1416 * altura)
    print("area =", area)