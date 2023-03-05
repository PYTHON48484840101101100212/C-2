# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:16:31 2023

@author: Coder
"""
import sys

liste = ['Engin',0,3,"6"]
for x in liste:
    try:
        print("Sayi: "+ str(x))
        sonuc = 1/int(x)
        print("Sonuc: "+ str(sonuc))
    except ValueError:
            print(str(x) + "Bir sayi degil")
    except ZeroDivisionError:
        print(str(x) + " icin sifira bolme hatasi ")
    except:
        print(str(x) + " Hesaplanamadi! ")
        print("Sistem Diyor ki: " + str(sys.exc_info()[0]))
    finally:
        print("İslemler Bitti!")
    