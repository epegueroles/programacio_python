# RO_Pag83_ex3.py
from math import *

a = int(input("Primer nombre de tres xifres  = "))
b = int(input("Segon nombre de tres xifres = "))

a2 = a // 10
nombre_del_mig_a = a2 % 10
b2 = b // 10
nombre_del_mig_b = b2 % 10
suma = nombre_del_mig_b + nombre_del_mig_a

print("La suma dels dos nombres es =", suma)