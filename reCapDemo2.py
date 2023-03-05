# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:51:37 2022

@author: Coder
"""

sayi = int (input("Lutfen bir sayi giriniz?"))

asalMi = True

for x in range (2,sayi):
    
    if (sayi % x ==0):
        asalMi = False
        
if asalMi:  # asalMi = True:   #ile ayni seydir.  

    print("Bu sayi asaldir.")

else:

    print("Bu sayi asal degildir.")      