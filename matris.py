# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 17:02:53 2022

@author: Coder
"""

import random

m1 = [[0 for x in range(3)]  for y in range(3)]
m2 = [[0 for x in range(3)]  for y in range(3)]
mt = [[0 for x in range(3)]  for y in range(3)]

for i in range(3):
    for j in range(3):
          
        m1[i][j] =random.randint(1,11)
        m2[i][j] =random.randint(1,11)
        mt[i][j] = m1[i][j] + m2[i][j]
        
print(m1)

print("*************")

print(m2)
print("*************")
print(mt)            
        