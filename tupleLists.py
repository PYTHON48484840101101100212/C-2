# -*- coding: utf-8 -*-

tupleList = ("Woman","Man","The God",(),[])    # () icine yazilir.
# Bu veri yapisi performansli bir data saglar.
list = [(),[],1,2,3]

# tupleList icindeki veriler degistirilemez.
# list icindeki veriler degistirilebilir.

# tupleList[0] ="ADAM"  #_UUHH DEGISTIRILEMEDI.
list[2] =0 #_DEGISTIRILDI.

print(tupleList)
print(list)

tupleDeger1 = "KARARA KINDAR KIRAR SENI"
tupleDeger2 = "KARAR VERME PARAM SENI KARALAR",  #_',' e dikkat et virgul olmasaydı 
#tupleDeger2'de str sinifinda olacakti.
print(type(tupleDeger1)) #why class is not tuple , because ',' yok xkdjsas
print(type(tupleDeger2))

#Ayrıca tuple sinifinda bir nesne okurken yine ayni sekilde ',' de okunur.

print(tupleDeger1)

print(tupleDeger2) # Goruldugu gibi ',' de okundu.


