# RO_Pag41_ex1.py
# Ex 1

n = int(input("numero paquets="))
pes_m = 0

for i in range(1, n + 1):
    pes = int(input(f"pes del paquet en kg ="))
    if pes > pes_m :
        pes_m = pes

print("pes maxim dels paquets =",pes_m ,"kg")