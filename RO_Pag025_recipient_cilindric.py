# RO_Pag25_recipient_cilindric.py
# Ex 2
litres = float(input(" litres = "))
altura = float(input(" altura = "))


volum = litres / 1000
radi= (volum / (altura * 3.1416)) ** 0.5
diametre_base = 2 * radi

print(" diametre_base = ", diametre_base, "m")