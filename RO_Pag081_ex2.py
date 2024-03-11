# RO_Pag81_ex2.py
from math import *

litres = int(input("litres="))
altura= int(input("altura="))

radi = sqrt(litres / (pi*altura))
diametre = radi * 2
print("diametre =",diametre)