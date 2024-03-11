# RO_Pag83_ex1.py
from math import *

dia = int(input("dies="))
anyy = 365
mes = 30

x = (anys,mesos)=divmod(dia,anyy)
y = (mesos,dies)=divmod(mesos,mes)

print(f"{dia} Dies equivalen a {anys} anys , {mesos} mesos i {dies} dies ")