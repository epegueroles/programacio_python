# RO_Pag032_ValorTemperatura.py


t = float(input(" temperatura ="))
code = int(input("Escull 1 o 2 ="))

if code  == 1 :
    c = 5 / 9 * (t - 32)
    print(" C =",c)

else :
    if code == 2 :
        f = 32 + (9 * t / 5)
        print(" f =", f)
    else:
        print("Error")
