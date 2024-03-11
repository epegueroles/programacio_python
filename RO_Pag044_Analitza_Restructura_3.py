# RO_Pag44_Analitza_Restructura_3.py
# Ex 3
import time

a = int(input(" a="))
b = int(input(" b="))
c = int(input(" c="))
r = 0

while a <= b and c > 0 :
    if b % 2 == 0:
        b = b - 1
        print(a, b, c, r)
        time.sleep(5)
    else:
        r = r + c
        b = b - 1
        print(a, b, c, r)
        time.sleep(5)
print(r)
        
        
    