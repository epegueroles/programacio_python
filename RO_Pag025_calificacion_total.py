# RO_Pag25_calificacion_total.py
# Ex 5

e = float(input("examen="))
ll = float(input("llicons="))
d1 = float(input("deures1="))
d2 = float(input("deures2="))
d3 = float(input("deures3="))

dT = ((d1 + d2 + d3) / 3)

examen = ((e * 70) / 10)
lliurement = ((ll * 20) / 10)
deures = ((dT * 10) / 10)

calificacio = (examen + lliurement + deures)

print(" calificació T=", calificacio)
