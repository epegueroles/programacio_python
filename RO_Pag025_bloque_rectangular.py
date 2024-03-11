# RO_Pag25_bloque_rectangular.py
# Ex 3
altura = float(input(" altura = "))
base = float(input(" base = "))


areaC = base ** 2
areaR = base * altura

areaT = 4 * areaR + 2 * areaC

volum = areaC * altura


print(" area total = ", areaT, "m^2")
print(" volum = ", volum, "m^3")