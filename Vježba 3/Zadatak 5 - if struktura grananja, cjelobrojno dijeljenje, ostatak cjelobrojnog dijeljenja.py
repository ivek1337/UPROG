print("Dimenzije terase a*a u metrima:")
print("-" *30)
a = int(input("a="))    #Unos dimenzija terase
mucm = a * 100  #m -> cm
print("\nDimenzije plocice c*d u centimetrima: ")
print("-" *30)
c = int(input("c="))    #duljina
d = int(input("d="))    #sirina
ukpl1 = (mucm // c) #terasa u cm / duljina za broj cijelih plocica
ukpl2 = (mucm // d) #terasa u cm / širina za broj cijelih plocica
ukpl10 = ukpl1  #nova varijabla za sveukupni broj plocica
ukpl20 = ukpl2  #nova varijabla za sveukupni broj plocica
if (ukpl1 % 2 != 0):    #ako broj cijelih plocica u duljini ima ostatak dodaj jos jednu
    ukpl10 = ukpl1 + 1
if (ukpl2 % 2 != 0):    #ako broj cijelih plocica u sirinu ima ostatak dodaj jos jednu
    ukpl20 = ukpl2 + 1
print("\nZa poplocati cijelu terasu trebate kupiti {} plocica.".format(ukpl10*ukpl20))
print("Na terasi ce biti {} cijelih plocica.".format(ukpl1*ukpl2))
