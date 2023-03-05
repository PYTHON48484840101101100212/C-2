 # -*- coding: utf-8 -*-

# ogrenciler =[str(input("Ogrenci isimlerini giriniz: "))]

# print(ogrenciler[1])


ogrenciler = ["Tahir","Omer","Enise","Rahim"]

ogrenciler.append("Ayse")

print(ogrenciler[4])

print("Kac Tane Tahir isimli Ogrenci Var? ",ogrenciler.count("Tahir"))

print(ogrenciler)

ogrenciler.remove("Ayse")

print(ogrenciler)

evler = list(("Adana","Artvin","Karabuk","Mersin"))

print(evler)

print(len(evler))

print("Mersin index'i: ",evler.index("Mersin"))

evler.pop(1)
print(evler)
evler.insert(0,"Antalya")
print(evler)

evler.reverse()

print(evler) 

print("--------")

evler5 = evler.copy()

evler2 = evler
evler2[1] = "Izmir"

print(evler2)
print(evler)
print(evler5)

print("--------")

evler.extend(evler5)

evler.sort()
# evler.reverse()
#evler listesinde sort komut'u ile alfabeye gore dizilim yaptik daha sonra
# reverse komut'u ile alfabeyi tersten okumasini sagladik.
print(evler)