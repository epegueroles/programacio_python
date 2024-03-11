#  RO_Pag45_Analitza_Restructura_4.py
# Ex 4

a = float(input(" a ="))
b = float(input(" b ="))
x = 0

if a < 5 :
    x = x + a - b
else : 
    while x < b :
       x = x + a
print("x=", x)