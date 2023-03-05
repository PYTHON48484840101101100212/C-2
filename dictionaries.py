# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:02:09 2022

@author: Coder
"""

sozluk1 = {
    
    "book" : "kitap",
    "table" :   "masa"
    
    }

sozluk2 = dict(key  ="anahtar",hair ="saç")

print(sozluk1)
print(sozluk1["book"])
sozluk1["pencil"] = "kalem"
print(sozluk1)
print(sozluk2)

del(sozluk1["table"])
print(len(sozluk1))
