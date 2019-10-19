R1 = int(input("Unesite vrijednost R1: "))
R2 = int(input("Unesite vrijednost R2: "))
print("\n"+"-" *20)
print("1. serijski spoj")
ser = R1 + R2
par = (R1 * R2)/ (R1 + R2)
print("2. paralelni spoj")
print("-" *20)
izbor = int(input("Vas odabir je: "))
if izbor == 1:
    print("Ukupan serijski otpor je {} om-a.".format(ser))
elif izbor == 2:
    print("Ukupan paralelni otpor je {} om-a.".format(par))
else:
    print("Niste odabrali niti jedan od ponudenih izbora.")
    
