# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:57:24 2023

@author: Coder
"""

try:
    sayi = int(input("Sayi Giriniz: "))
    
except ValueError:
    print("Tip Uyusmazligi! Lutfen bir Sayi Giriniz: ") 
except ZeroDivisionError:
    print("Payda Sifir Olamaz! ")
except:
    print("Bir hata olustu!")
print("Bitti")    