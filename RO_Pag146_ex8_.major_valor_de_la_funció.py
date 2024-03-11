# RO_Pag146_ex8_.major_valor_de_la_funció.py
from math import *
x = 1
n = float(input("fins quin num vols calcular? : "))
major_n_f = 0
f = 0
while x != n and x < n:
    f = sin(x) + log(x)
    
    if f > major_n_f:
        major_n_f = f
        print(major_n_f)
    x = x + 0.1

print("El máxim valor de la funció és :",major_n_f)