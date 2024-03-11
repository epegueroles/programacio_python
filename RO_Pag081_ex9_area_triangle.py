# RO_Pag81_ex9_area_triangle.py
from math import *

a = 2
b = 4

c = 4
d = 2

x = sqrt(pow((c-a),2) + pow((d-b),2)) # de c-a al punt d-b
y = sqrt(pow(a,2)+pow(b,2)) # de a al punt b
z = sqrt(pow(c,2)+pow(d,2)) # de c al punt d

area_quadrat =  c * b
area_2 = 4 * 2 / 2
area_3 = 2 * 4 / 2
area_4 = 2 * 2 / 2

area_triangle = area_quadrat - (area_2 + area_3 + area_4)

print(area_triangle,"m2")