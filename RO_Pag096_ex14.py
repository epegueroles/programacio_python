# RO_Pag096_ex14.py
from math import *

l = float(input("llargada :"))
a = float(input("amplada :"))
h = float(input("haltura :"))
d = float(input("Diametre pel que ha de passar o no una de les diagonals :"))

d1 = sqrt(pow(h,2)+pow(a,2))
print(d1,"diagonal 1")
d2 = sqrt(pow(h,2)+pow(l,2))
print(d2,"diagonal 2")
d3 = sqrt(pow(l,2)+pow(a,2))
print(d3,"diagonal 3")

if d < d1 and d < d2 and d < d3 :
    print("El rectangle no passara")
elif d >= d1 :
    print("El rectangle si que passara")
elif d >= d2 :
    print("El rectangl si que passara")
elif d >= d3 :
    print("El rectangle si que passara")