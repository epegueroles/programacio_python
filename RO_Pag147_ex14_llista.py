# RO_Pag147_ex14_llista.py
from math import *

articles = [454,785,1000,2347]
diners = float(input("diners que tens : "))
articles_comprar = 0
a = 0
d = 0
for n in articles :
    if n <= diners :
        a += 1
        articles_comprar = diners / n // 1 
        print(f"Pots comprar {articles_comprar} unitats de l'erticle {a}")
        
    else :
        print("No ho pots cpmprar")
print(f"En total pots comprar {a} articles")