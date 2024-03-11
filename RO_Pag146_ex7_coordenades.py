# RO_Pag146_ex7_coordenades.py
from math import *
#7.- Lea las coordenadas de u, v de la ubicación de una fábrica y las coordenada x, y de n
#sitios de distribución. Encuentre cual es la distancia del sitio más alejado de la fábrica

u = float(input("cordenada x de la fabrica"))
v = float(input("cordenada y de la fabrica"))
n = float(input("quants punts de distribució hi ha? "))
z = 0
punt_més_llarg = 0
while z != n:
    
    x = float(input("cordenada x del punt de distribució"))
    y = float(input("cordenada y del punt de distribució"))
    
    xy = sqrt(pow(x-u,2) + pow(y-v,2))
    
    if xy > punt_més_llarg:
        punt_més_llarg = xy
        
    elif xy < punt_més_llarg:
        punt_més_llarg = punt_més_llarg
        
    z = z + 1
        
print("el punt mes llarg medeix", punt_més_llarg)