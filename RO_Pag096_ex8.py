# RO_Pag096_ex8.py
from math import *

calificacio1 = float(input(" La primera calificació de l'estudiant 1 és:"))
calificacio2 = float(input(" La segona calificació de l'estudiant 1 és:"))
calificacio3 = float(input(" La tercera calificació de l'estudiant 1 és:"))

calificacio4 = float(input(" La primera calificació de l'estudiant 2 és:"))
calificacio5 = float(input(" La segona calificació de l'estudiant 2 és:"))
calificacio6 = float(input(" La tercera calificació de l'estudiant 2 és:"))
suma1 = 0
suma2 = 0
#estudiant 1
if calificacio1 == calificacio2 and calificacio2 == calificacio3 :
    print("totes les qualificacións son iguals")
elif calificacio1 >= calificacio2 and calificacio2 >= calificacio3 :
    suma1 = calificacio1 + calificacio2
elif calificacio3 >= calificacio1 and calificacio1 >= calificacio2 :
    suma1 = calificacio3 + calificacio1
elif calificacio2 >= calificacio3 and calificacio3 >= calificacio1 :
    suma1 = calificacio2 + calificacio3
    print(suma1)

#estudiant 2
if calificacio4 == calificacio5 and calificacio5 == calificacio6 :
    print("totes les qualificacións son iguals")
elif calificacio4 >= calificacio5 and calificacio5 >= calificacio6 :
    suma2 = calificacio4 + calificacio5
elif calificacio6 >= calificacio4 and calificacio4 >= calificacio5 :
    suma2 = calificacio6 + calificacio4
elif calificacio5 >= calificacio6 and calificacio6 >= calificacio4 :
    suma2 = calificacio5 + calificacio6
    print(suma2)

# ara fem la comparacio
if suma1 > suma2 :
    print(f"el primer estudiant {suma1} te mes bona qualificació que el segon{suma2}")
elif suma1 == suma2 :
    print("els dos estudiants tenen la mateixa nota")
elif suma2 > suma1 :
    print(f"el segon estudiant {suma2} te mes bona qualificació que el primer{suma1}")
