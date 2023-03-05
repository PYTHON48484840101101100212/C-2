# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:49:18 2023

@author: Coder
"""

def topla(x,y):
    return x + y
def cikar(x,y):
    return x - y
def carp(x,y):
    return x * y
def bol(x,y):
    return x / y


print ("********CALCULATOR 2023********")
print("1: TOPLAMA")
print("2: CIKARMA")
print("3: CARPMA")
print("4: BOLME")

number = input("Please want a number: ")
x = int(input("Please take a number: "))
y = int(input("Please take a number: "))


    

if number == '1':
     print("Toplam: "+str(topla(x, y)))
      
elif number == '2':
      print("Cikartma: "+str(cikar(x, y)))
      
elif number == '3':
       print("Carpim: "+str(carp(x, y)))
      
elif number == '4':
      print("Bolum: "+str(bol(x, y)))
      
else :
    print("Gecersiz Secenek!..")      