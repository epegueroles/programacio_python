# RO_Pag097_ex19.py
from math import *

j1 = int(input("Primer jutge :"))
j2 = int(input("Segon jutge :"))
j3 = int(input("Tercer jutge :"))
# 011
if j1 == 0 and j2 == 1 and j3 == 1 :
    print("Continua")
# 101
elif j1 == 1 and j2 == 0 and j3 == 1 :
    print("Continua")
# 110
elif j1 == 1 and j2 == 1 and j3 == 0 :
    print("Continua")
# 111
elif j1 == 1 and j2 == 1 and j3 == 1 :
    print("continua")
# 000 o si te un 1 i dos 00
else :
    print("No continua")