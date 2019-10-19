print("Unesite vrijeme pocetka filma:")
pocsat=int(input("Sat: "))      #Unos pocetnog sata
pocmin=int(input("Minute: "))       #Unos pocetnih minuta
print("\n")
print("Unesite vrijeme zavrsetka filma:")
zavsat=int(input("Sat: "))      #Unos zavrsnog sata
zavmin=int(input("Minute: "))       #Unos zavrsnih minuta
print("\n")
print("\n")
satuminpoc=pocsat*60+pocmin     #pretvaranje pocetnih sati u minute + dodavanje pocetnih minuta
satuminzav=zavsat*60+zavmin     #pretvaranje zavrsnih sati u minute + dodavanje zavrsnih minuta
raz=satuminzav-satuminpoc       #ralika izmedu zavrsetka i pocetka
print("Trajanje filma: {}h\t{}min".format(raz//60,raz%60))      #raz//60 --> cjelobrojno dijeljenje || raz%60 --> cjelobrojni ostatak
