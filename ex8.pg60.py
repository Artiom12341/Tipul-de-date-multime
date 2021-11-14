"""PROGRAMEAZĂ! Scrieţi un program care citeşte de la tastatură elementele
mulţimilor A şi B şi afişează pe ecran:
a) intersecţia mulţimilor A şi B;
b) reuniunea mulţimilor A şi B;
c) diferenţa mulţimilor A şi B.
	 Mulţimile A şi B sunt formate din numere întregi."""
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
print("a) intersecţia mulţimilor A şi B",a.intersection(b))
print('b)reuniunea multimilor A si B:',a.union(b))
print('c)diferenta multimilor A si B:',a.difference(b))
print('d)diferenta multimilor B si A:',b.difference(a))