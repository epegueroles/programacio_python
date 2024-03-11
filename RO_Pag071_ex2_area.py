# RO_Pag71_ex2_area.py
from math import *

diagonal = 5
angle = 40

angle_rad = angle * (pi/180) # passem a radiants
base = 5 * cos (angle_rad)
altura = 5 * sin (angle_rad)

area = (base * altura) / 2

print("area=",area,"cm2")