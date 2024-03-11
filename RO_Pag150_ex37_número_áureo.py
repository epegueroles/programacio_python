# RO_Pag150_ex37_número_áureo.py
from math import*

n = int(input("n ="))
print("Parelles de números (a,b) entre 1 i n")
print("=====================================")
parelles_num_aureos = 0
for a in range(1,n + 1):
    for b in range(1,n + 1):
        print("(a,b)=", a, b)
        if (a + b) / b == a / b:
            parelles_num_aureos += 1
            print(f"Una parella aureo és {a} i {b}. ")
            print("Hi ha ",parelles_num_aureos," parelles de numeros aureos.")
if parelles_num_aureos == 0:
    print("No tenim ca parella aurea")