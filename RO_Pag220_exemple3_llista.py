# RO_Pag220_exemple3_llista.py
from random import *
def vectmax():
    v = [randint(0,10) for i in range(8)]
    print(v)
    n = len(v)
    r = v[0]
    p = 0
    for i in range(0,n):
        if v[i] > r:
            r = v[i]
            p = i
    return r,p