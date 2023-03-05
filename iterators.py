# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 11:50:21 2023

@author: Coder
"""

sehirler = ["Istanbul","Ankara","Izmir","Adiyaman"]
iteratorum = iter(sehirler)

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))

# Alttaki de bir iteratordur

for sehir in sehirler:
    print(sehir)