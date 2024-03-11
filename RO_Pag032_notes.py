#RO_Pag32_notes.py
# Ex 5

calificacio_1 = float(input("calificació_1 ="))
calificacio_2 = float(input("calificacio_2 ="))
calificacio_3 = float(input("calificacio_3 ="))

if calificacio_1 > calificacio_2 and calificacio_1 > calificacio_3 :
    print("calificacio_1 =", calificacio_1)
elif calificacio_2 > calificacio_3 and calificacio_2 > calificacio_1 :
    print("calificacio_2 =", calificacio_2)
else :
    print("calificacio_3 =", calificacio_3)
