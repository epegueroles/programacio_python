# RO_Pag38_Exemple.py

n = int(input("n ="))
s = 0

for i in range(1, n + 1) :
    k = 2 * i -1
    s = s + k
    print("cicle", i ,"impar", k ,"suma_impars", s )

    if s ==n**2 :
        print("verdadero")
    
    else :
        print("falso")