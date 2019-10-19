c=float(input("Unesite iznos odobrenog potrošaèkog kredita: "))
p=float(input("Unesite godišnju kamatnu stopu: "))
m=int(input("Unesite broj mjeseci: "))
k=(c*p*(m+1))/2400
print("Vaša kamata je: ",k)
