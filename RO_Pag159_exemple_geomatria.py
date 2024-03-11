# RO_Pag159_exemple_geomatria.py
from math import*
def quadrat(x):
    A = pow(x,2)
    P = 4 * x
    print("Area",A)
    print("Perimetre",P)
def triangle(a,b,c,h):
    A = b * h / 2
    P = a + b + c
    print("Area",A)
    print("Perimetre",P)
def rectangle(a,b):
    A = a * b
    P = a*2 + b*2
    print("Area",A)
    print("Perimetre",P)
def paralelogram(a,b):
    A = a * b
    P = a*2 + b*2
    print("Area",A)
    print("Perimetre",P)
def rombo(D,d,a):
    A = D*d/2
    P = 4*a
    print("Area",A)
    print("Perimetre",P)
def cometa(a,d,D,b):
    A = D*d/2
    P = 2*(b + a)
    print("Area",A)
    print("Perimetre",P)
def trapecio(a,b,c,h,B):
    A = (B+b)*h / 2
    P = B+b+a+c
    print("Area",A)
    print("Perimetre",P)
def circulo(pi,r):
    A = pi * r**2
    P = 2 * pi * r
    print("Area",A)
    print("Perimetre",P)
def poligonregular(a,b,n):
    P = n * b
    A = P * a / 2
    print("Area",A)
    print("Perimetre",P)
def coronacircular(pi,R,r):
    A = pi*(R**2 - r**2)
    print("Area",A)
def sectorcircular(R,n):
    A = pi * R**2 * n / 360
    print("Area",A)
sortida = False
while not sortida:
    print("")
    print("")
    print("")
    print("tria quina figura geometrica vols calcular l'area, volums i perímetres en cm : ")
    print("cuadrat 1")
    print("triangle 2")
    print("rectangle 3")
    print("paralelogram 4")
    print("rombo 5")
    print("cometa 6")
    print("trapecio 7")
    print("cercle 8")
    print("poligon rectangular 9")
    print("corona circular 10")
    print("sector circular 11")
    print("Si vols surtir del bucle, pulsa 12")
    opcio = int(input("Quina figura vols calcular? "))
    
    if opcio == 1:
        x = float(input("Costat del cuadrat :"))
        quadrat(x)
    elif opcio == 2:
        a = float(input("Costat 1 del triangle :"))
        b = float(input("Costat 2 del triangle :"))
        c = float(input("Costat 3 del triangle :"))
        h = float(input("Alçada del triangle :"))
        triangle(a,b,c,h)
    elif opcio == 3:
        a = float(input("Costat 1 del rectangle :"))
        b = float(input("Costat 2 del rectangle :"))
        rectangle(a,b)
    elif opcio == 4:
        a = float(input("Base del paralelogram :"))
        b = float(input("Altura del paralelogram :"))
        paralelogram(a,b)
    elif opcio == 5:
        D = float(input("Distancia mes llarga del centre de rombo a la punta :"))
        d = float(input("Distancia mes curta del centre de rombo a la punta :"))
        a = float(input("Costat del rombo :"))
        rombo(D,d,a)
    elif opcio == 6:
        a = float(input("Costat  petit del cometa :"))
        d = d = float(input("Distancia mes curta del centre del cometa a la punta :"))
        D = float(input("Distancia mes llarga del centre del cometa a la punta :"))
        b = float(input("Costat gran del cometa :"))
        cometa(a,d,D,b)
    elif opcio == 7:
        a = float(input("Costat del trapesi :"))
        b = float(input("Base petita del trapesi :"))
        c = float(input("Costat del trapesi :"))
        h = float(input("Haltura del trapesi :"))
        B = float(input("Base gran del trapesi :"))
        trapecio(a,b,c,h,B)
    elif opcio == 8:
        r = float(input("Radi :"))
        circulo(pi,r)
    elif opcio == 9:
        a = float(input("Apotema del poligon rectangular :"))
        b = float(input("Costat del poligon rectangular :"))
        n = float(input("Numero de costats :"))
        poligonregular(a,b,n)
    elif opcio == 10:
        R = float(input("Radi de la corona circular :"))
        r = float(input("Radi que se li restara a la rodona :"))
        coronacircular(pi,R,r)
    elif opcio == 11:
        R = float(input("Radi del sector circular :"))
        n = float(input("Angle que cols calular :"))
        sectorcircular(R,n)
    elif opcio == 12:
        sortida = True
    else:
        print("error")