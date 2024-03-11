# RO_Pag148_ex29_número_magic.py
from math import *

dia = int(input("dia "))
mes = int(input("mes "))
anyy = int(input("any "))

numero_magic = dia + mes + anyy

a = numero_magic // 1000
b = numero_magic // 100 % 10
c = numero_magic // 10 % 10
d = numero_magic % 10

numero_magic = a + b + c + d
if numero_magic >= 10 :
    f = numero_magic // 10
    g = numero_magic % 10
    numero_magic = f + g
else :
    numero_magic = numero_magic
print(f"el teu numero magic es el {numero_magic} .")