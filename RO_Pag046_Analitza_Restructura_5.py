# RO_Pag46_Analitza_Restructura_5.py
# Ex 5

a = float(input(" a="))
b = float(input(" b="))
c = float(input(" c="))

if a > b :
    while c <= a :
        c = c + 3
else :
    while a < b + c :
        a = a + 5
    print("a =", a)
print("c =", c)