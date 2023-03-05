# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 12:30:29 2022

@author: Coder
"""

class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    
    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2
    
    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2
    
math = Matematik()

print("Toplam = " + str(math.topla(2,4)))

print("Cikar = " + str(math.topla(2,4)))

print("Carpim = " + str(math.topla(2,4)))

print("Bolum = " + str(math.topla(2,4)))
class Person:
    def _init_(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Enes","ORHAN",19)
print(person1)

class Worker(Person):
    def _init_(self,salary):
        self.salary = salary
        
class Customer(Person):
    def _init_(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
ali = Worker()
veli = Customer()  
