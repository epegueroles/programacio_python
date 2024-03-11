# RO_Pag180_ex2_primo.py
from random import*

def primo():
    surt = False
    while surt == False:
        n = 0  
        a = randint(1, 100)
        b = randint(1, 100)
        x = a + b
        for i in range(1, 101):
            if x % i == 0:
                n = n + 1
        if n > 1:
            print(x, "No és un numero primer")
            surt = False
        elif n == 1:
            print(x, "És un numero primer")
            surt = True
    