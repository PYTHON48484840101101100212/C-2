class Person:
    def _init_(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("EnesMi","ORHAN",19)
print(person1.firstName)
class Worker(Person):
    def _init_(self,salary):
        self.salary = salary
        
class Customer(Person):
    def _init_(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
ali = Worker()
veli = Customer()        
    