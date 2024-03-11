# RO_Pag41_ex6.py
# ex 6
grans_blat = 0

for i in range(64):
    grans_blat += 2**i
grans_kg = grans_blat / 20000
grans_tones = grans_blat / 1000

print("grans = ",grans_tones)