# RO_Pag28_prueba.py
# Prova

n = int(input(" quantitat_llantas = "))
p = float(input("preu_inicial_unitat = "))

if n > 4:
    p = 0.9 *  p
    t = n * p
else: t = n * p

print(" total = ", t)
print(" Sortida = ", t )