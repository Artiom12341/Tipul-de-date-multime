"""Elaboraţi un program care afişează pe ecran toate submulţimile mulţimii
{’A’, ’B’, ’C’, ’D’}."""
import itertools
a={'A','B','C','D'}
b=[]
for i in range(0,len(a)):
    s=itertools.permutations(a,i)
    b+=s
print(b)