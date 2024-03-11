# RO_Pag096_ex10.py
from math import *

a = float(input("costat 1 del triangle ="))
b = float(input("costat 2 del triangle ="))
c = float(input("costat 3 del triangle ="))

if a == b and b == c :
    print("El triangle és equilater")
elif a == b and c != a :
    print("El triangle és isòseles")
elif b == c and a != b :
    print("El triangle és isòseles")
elif c == a and c != b :
    print("El triangle és isòseles")
elif a != b and a!= c and c != b :
    print("El triangle és escalè")