# RO_Pag30_Pago_Setmanal.py
# Proba

c = float(input(" quantitat_hores = "))
t = float(input(" tarifa_hora = "))
d = float(input(" desconta_pago_setmanal = "))
p = 0

if c <= 40 :
    p = c * t - d
else :
    p = 40 * t + (1.5 * t * (c - 40)) - d

print(" paga = ", p)