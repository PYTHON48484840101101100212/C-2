# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

mesaj= "Hello World"

kaifuku = "Behlül"

nani= "OPEN THE DOOR"

print(len(mesaj))

print(mesaj)

yeniMesaj = mesaj[5]

print (yeniMesaj)

print(mesaj[0:11])


yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

print("\n")

nani = nani.lower()

nani = nani.replace("o","a")

mesaj = mesaj.upper()

kaifuku = kaifuku.replace("ü","u")

print(mesaj)

print(kaifuku)

print(nani)
print("")

bilgi = "       Enes ORHAN 19 Adana              " .strip()

print(bilgi.split())
print(bilgi.split(" "))
print("SoyAdı: "+bilgi.split()[1])

input("İsim: ")

input("Soyİsim: ")
                
input("DogumTarihi: ")

input("Memleket: ")
print("♥")

