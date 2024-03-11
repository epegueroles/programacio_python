# RO_Pag096_ex12.py
from math import *

preu = float(input("preu producte ="))
quantitat_articles = float(input("quantitat articles que agafaras :"))
desconte = 0
if quantitat_articles > 5 and quantitat_articles < 10 :
    desconte = (preu * quantitat_articles) * 0.05
elif quantitat_articles >= 10 :
    desconte = (preu * quantitat_articles) * 0.08
preu_total = (preu * quantitat_articles) - desconte
print(f"el preu total amb el desconte incluit es : {preu_total}")