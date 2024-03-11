# RO_Pag41_ex3.py
# Ex 3

n = int(input("n="))
a = 0
b = 1
suma = 0

for i in range(n-1):
    print("b =",b)
    c = a + b
    a = b
    b = c
    suma = b + suma
suma = suma + 1 

print("b =",b)
print(" suma =",suma)