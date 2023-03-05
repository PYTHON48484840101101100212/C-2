# -*- coding: utf-8 -*-

setA ={1,2,3,4,5}
setB ={1,3,5,6,7,8,9}


# A VE B KUMESİNDEKİ TUM DATALARI GOSTERIR.
# Union Gosterimi iki farkli sekilde yapilabilir.


print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))
# Set komutu sayilari da  kendi algoritmasina gore dizer.


print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))
# A VE B KUMESINDEKI DATALARIN ORTAK KUMESINI GOSTERIR.


print(setA - setB)
print(setB -setA)
print(setA.difference(setB))
print(setB.difference(setA))
# IKI KUME FARKI 


print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA)) 
# YINE IKI KUME FARKI ANCAK A VE B'DE FARKLI OLANLARIN HEPSINI BERABER YAZAR.