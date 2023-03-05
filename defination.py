# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 13:43:11 2022

@author: Coder
"""
def pusd(isim = " Sayın Ziyaretçi" , soyIsım = " Siteme Hoşgeldiniz:)" ):

     print("Merhaba" , isim + soyIsım)
          

pusd(" Engin" , " Yalcin")
pusd()
pusd("Enes")
pusd()


#Deger Return Eden Fonksiyonlar: 
    
    
def DikUcgenAlaniHesapla(a,b):
    
    return (a*b/2)

alan = DikUcgenAlaniHesapla(8,9)

print("Alan =" ,alan)

#Ya da lambda fonksiyonu ile Return Edebiliriz:)


DikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print("Alan = " , DikUcgenAlaniHesapla2(4,5))
print(type(DikUcgenAlaniHesapla2))

Z = DikUcgenAlaniHesapla2
print(Z(9,8))