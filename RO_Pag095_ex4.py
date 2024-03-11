# RO_Pag95_ex4.py
from math import *

n = int(input("numero dos xifres ="))
(x,y)=divmod(n,10)
nombre = x + y
if nombre % 2 == 0 :
    print(f"El número {nombre} és parell :)")
elif nombre % 2 != 0 :
    print(f"El número {nombre} no és parell :(")