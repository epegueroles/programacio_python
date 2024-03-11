# RO_Pag97_ex21.py
from math import *

a11 = float(input("primer valor matriu ="))
a12 = float(input("segon valor matriu ="))
a21 = float(input("primer valor matriu segona columna ="))

a22 = (a21 * a12) / a11
det_matriu = (a11 * a22) - (a21 * a12)

print(f"{a22} el nombre que falta de la matriu, {det_matriu} si és 0 vol dir que està be")