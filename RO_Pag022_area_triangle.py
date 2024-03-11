# RO_PO22_area_triangle.py
import math # llibreria de Python

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

t = (a+b+c)/2 # variables
s = math.sqrt(t*(t-a)*(t-b)*(t-c)) # càlculs
print("t = ", t)
print("s = ", s) #sortida de dades
