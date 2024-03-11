# RO_Pag096_ex11.py
from math import *

a = float(input("absises :"))
o = float(input("ordenada :"))
a2 = float(input("absises :"))
o2 = float(input("ordenada :"))
punt1 = sqrt(pow(a,2)+pow(o,2))
punt2 = sqrt(pow(a2,2)+pow(o2,2))
if punt1 < punt2 :
    print("punt 1")
elif punt2 < punt1 :
    print("punt 2")
else :
    print("igual")