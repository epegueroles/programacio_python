# RO_Pag83_ex5.py
from math import *

z = int(input("diners ="))
x = (a,b)=divmod(z,100)
y = (c,d)=divmod(b,50)
n = (e,f)=divmod(d,20)
m = (g,h)=divmod(f,10)
n = (i,j)=divmod(h,5)
w = (k,l)=divmod(j,1)

print(f"{a} billets de 100, {c} billets de 50, {e} billets de 20, {g} billets de 10, {i} billets de 5, i {k} billets de 1")