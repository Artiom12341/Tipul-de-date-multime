""" Elaboraţi un program care afişează pe ecran toate submulţimile mulţimii {1, 2,
3, 4}."""
import itertools
a={1,2,3,4}
b=[]
for i in range(0,len(a)):
    s=itertools.combinations(a,i)
    b+=s
print(b)