# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:24:13 2022

@author: Coder
"""

studentsSet = {"Ismail","Emir","Mete","Enes"}
# Bunu su sekilde de yapabiliriz.


print(studentsSet)

# ya da bunu şu şekilde de print edebiliriz dmanscöjasnkjcasmnmdflkw(CICIKLIK AX LE-VEL):) PUAHAHAHA

for student in studentsSet:
    
    print(student)
    
# Bir sey dikkatini cekti mi? 
# Set , verileri hizli getirecek sekilde kendine has bir algoritmaya göre siralar ve read eder.

print("Ismail " in studentsSet)   #-"Derin" yerine "derin" yazarsak hata verir.
# "Derin " gibi bosluk birakip yaparsan da hata verir.

    
if "Emir " in studentsSet:
        
        print("Listede Var")
    
else:
     print("Listede Yok")
     
studentsSet.update(["Isa","Mehmet","Yakar","Apo"])    
    
print(studentsSet)  # Goruldugu gibi yine kendine has bir algoritmaya gore siraladi.

studentsSet.add("Ali")

print(studentsSet)


# studentsSet.remove("Derin") 
#program yazarken set'in icinde olmayan bir sey yazarsak hata verir.
#Onun yerine hata vermesini istemiyorsak .discard komutunu kullaniriz.

studentsSet.discard("Derin") 
# Goruldugu gibi "Derin" olmamasina ragmen hata vermedi ahhaahahahaha

studentsSet.remove("Ali")

print(len(studentsSet))

studentsSet.pop() 
# Rastgele bir Veriyi siler.
print(len(studentsSet))
print(studentsSet)

studentsSet.clear()
#Tum veri setini siler.
print(studentsSet)
#Ya da direkt set'i silmek istersek del komutunu kullaniriz.

del studentsSet
# print(studentsSet)
#Bu komutu kullanirsan print bile edemezsin.Cunku sildigi sey bellekten silinir.


