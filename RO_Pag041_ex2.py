# RO_Pag41_ex2.py
# Ex 2

n = int(input("numero de presones que voten ="))
print("a favor = 1")
print("en contre = 0")
vots_a_favor = 0
vots_en_contra = 0
vots_nuls = 0

for i in range (1, n + 1) :
    vot = int(input("vot "))
    if vot == 1 :
        vots_a_favor = vot + vots_a_favor
    elif vot == 0 :
        vot = 1
        vots_en_contra = vot + vots_en_contra
    else :
        vot = 1
        vots_nuls = vot + vots_nuls
print("vots a favor =",vots_a_favor)
print("vots en contra =",vots_en_contra)
print("vots nuls= ", vots_nuls)