# RO_Pag096_ex9.py
from math import *

nota1 = float(input("nota 1 ="))
nota2 = float(input("nota 2 ="))
nota3 = float(input("nota 3="))
 
if nota1 > nota2 and nota1 > nota3:
    if nota2 >= nota3:
        print(f"{nota1} es la nota més alta, i {nota3} la més baixa")
    else:
        print(f"{nota1} es la nota més alta, i {nota2} la més baixa")
elif nota2 > nota3 and nota2 > nota1:
    if nota3 >= nota1:
     print(f"{nota2} es la nota més alta, i {nota1} la més baixa")
    else:
        print(f"{nota2} es la nota més alta, i {nota3} la més baixa")
elif nota3 > nota2 and nota3 > nota1:
    if nota2 >= nota1:
        print(f"{nota3} es la nota més alta, i {nota1} la més baixa")
    else :
        print(f"{nota3} es la nota més alta, i {nota1} la més baixa")
elif nota1 == nota2 and nota3 == nota2:
    print("Les tres notes són iguals")
elif nota1 == nota2 and nota2 > nota3:
    print(f"{nota1} es la nota més alta, i {nota3} la més baixa")
elif nota1 == nota2 and nota2 < nota3:
    print(f"{nota3} es la nota més alta, i {nota1} la més baixa")
elif nota3 == nota2 and nota1 > nota3:
    print(f"{nota1} es la nota més alta, i {nota3} la més baixa")
elif nota3 == nota2 and nota1 < nota3:
    print(f"{nota3} es la nota més alta, i {nota1} la més baixa")
elif nota1 == nota3 and nota2 < nota3:
     print(f"{nota3} es la nota més alta, i {nota1} la més baixa")