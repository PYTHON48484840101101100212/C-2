# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:23:39 2022

@author: Coder
"""

sayi = int(input("Faktoriyeli Alinacak Sayiyi Giriniz: "))

faktoriyel = 1

if sayi<0 :
    print("Negatif Sayilarin Faktoriyeli Hesaplanamaz!")
    
elif sayi == 0: 
    print("Sonuc = 1 ")

elif sayi>0:
    for i in range(1,sayi+1):
        faktoriyel = i*faktoriyel
        
    print("Sonuc = ",faktoriyel)
    