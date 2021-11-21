x=int(input("Dati numarul de caractere din multimea A-"))
m=int(input("Dati numarul de caractere din multimea B-"))
a=set()
for i in range(x):
    c=int(input("Elementele multimii A sunt-"))
    a.add(c)
b=set()
for i in range(m):
    e=int(input("Elementele multimii B sunt-"))
    b.add(e)
print(a,b)
print('a) reuniunea multimilor A si B:',a.union(b))
print("b) intersecţia mulţimilor A şi B",a.intersection(b))
print('c) diferenta multimilor A si B:',a.difference(b))