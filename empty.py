# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:28:28 2023

@author: Coder
"""

ogrenciler = ["Engin","Derin","Salih","Enes","EMG"]

fileToAppend = open("ogrenciler","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
fileToAppend.close()
    
    