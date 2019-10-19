x=float(input("Unesite duljinu letvice u cm: "))
y=float(input("Unesite duljinu dijela u cm koji ce se izrezati: "))
z=x//y
q=x%y
print("Kolicina izrezanih dijelova: ",z,"\nLetvice preostalo: ",q)
