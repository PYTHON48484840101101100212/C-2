# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:00:22 2022

@author: Coder
"""

x = int(input("Bir Tamsayi Giriniz: "))
y = int(input("Bir Tamsayi Giriniz: "))
z = int(input("Bir Tamsayi Giriniz: "))

if (x>y) and (x>z):
    print(x, " Sayisi En Buyuktur.")
    
if (y>x) and (y>z):
    print(y ," Sayisi En Buyuktur.")    

if (z>y) and (z>x):
    print(z, " Sayisi En Buyuktur.")