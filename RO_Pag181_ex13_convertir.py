# RO_Pag181_ex13_convertir.py
from math import*

def polar(x,y):
        r = sqrt(pow(x,2) + pow(y,2))
        t = atan(y/x) * (180/pi)
        
        print(r,t)
def cartesiana(r,t):
        x = r * cos(t * (pi/180)) 
        y = r * sin(t * (pi/180)) 
        print(x,y)

print("Convertir a polar 1")
print("Convertir a cartesianas 2")
print("Surt 3")

n = int(input("Escull una opció : "))
surt = False
while not surt:
    if n == 1:
        x = float(input("x = "))
        y = float(input("y = "))
        polar(x,y)
        break
    elif n == 2:
        r = float(input("r = "))
        t = float(input("t = "))
        cartesiana(r,t)
        break
    else:
        surt = True
    