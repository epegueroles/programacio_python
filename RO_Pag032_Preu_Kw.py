# RO_Pag032_Preu_Kw.py
# ex 2

kw = float(input("kw ="))
preu_kw = float(input("preu_kw ="))

if kw > 700 :
    total = kw * preu_kw * 1.05
else :
    total = kw * preu_kw

print("total_a_pagar =",total)