# RO_Pag095_ex2.py
from math import *

radi = float(input("radi ="))
altura = float(input("altura ="))

if altura > radi :
    volum = 3.1416 * radi * radi * altura
    print("volum =", volum)
else :
    print("Error")