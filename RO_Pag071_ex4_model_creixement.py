# RO_Pag71_ex4_model_creixement.py
from math import *

k = (50 - (2 * exp(0.1*10))) / 10
print(k)
t = 10
f_t = k * t + 2 * exp(0.1*t)
print(f_t)