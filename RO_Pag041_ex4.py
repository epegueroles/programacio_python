# RO_Pag41_ex4.py
# Ex 4

n = int(input("quantitat de termes ="))
x = 1
pi = 0
for i in range (1, n) :
    if i % 2 == 0 :
        k = (1 / x) * (-1)
    else :
        k = (1 / x)
    x = x + 2
    pi = pi + k
    print("pi = ",pi)

pi = 4 * pi

print("pi = ",pi)
print("gracies per l'espera :)")