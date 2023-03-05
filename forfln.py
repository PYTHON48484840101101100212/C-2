# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:45:41 2022

@author: Coder
"""

sehirler = ["Adana","Izmir","Eskişehir","Antalya"]


for sehir in sehirler:
    print(sehir , "icin sehir kodu: " , sehir[0:3])
    
    if sehir == "Adana":
        print("01 BABAAA")
    elif sehir != "Adana":
        print("Rap Loading...")
        
        print("*********************")
        
        
numbers =  [0,1,2,3,4,5,6,7,8,9]

sum = 0

for val in numbers:
    
    sum = sum + val

print("The sum is: ",sum)    

print("*********************")
 
sayac = 1

sonuc = 0

while sayac<=10:
    
    sonuc = sonuc + sayac
    sayac = sayac + 1
    
    
print(sonuc)

print("*********************")

sehirler = ["Adana","Izmir","Eskişehir","Antalya"]

for sehir in sehirler:
    
    if sehir == "Izmir":
        
        continue  #break yazarsak sadece Adana yazar.
        
    print(sehir , "icin sehir kodu: " , sehir[0:3])

print("*********************")

for x in range(100):
    
    print(x)
