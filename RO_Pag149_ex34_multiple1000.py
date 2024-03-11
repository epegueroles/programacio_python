# RO_Pag149_ex34_multiple1000.py
a = int(input("Introdueix a entre 1 i 1000  "))
b = int(input("Introdueix b entre 1 i 1000  "))
for a in range ( a, a + 1):
    for b in range(b, b + 1):
        x = 1000 - a
        y = 1000 - b
        j = x + y
        h = 1000-j
        r1 = h * 1000
        r = x * y
        rfin = r + r1
        if rfin == a * b :
            print(f"El resultat del producte ({a},{b}) es : {rfin}")
        else :
            print(f"{rfin} es differet a {a * b}")
