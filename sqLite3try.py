# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:06:54 2023

@author: Coder
"""

import sqlite3

def selectoperations():
    
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute(""" select FirstName,LastName 
                                from Customers
                                where FirstName like '%a' """)
    for row in cursor:
        print("FirstName: "+ row[0])
        print("LastName: "+ row[1])
        print("*******************")                                                                                                
    connection.close()

# selectoperations()

def insertCustomer():
    connection = sqlite3.connect("chinook.db")     
    connection.execute("""(insert into customers 
                       (firstName,lastName,city,email)
                       values ('Enes','Orhan','Adana',
                               'enes0101@gmail.com')""")
    connection.commit()
    connection.close()    
# insertCustomer()                   
def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" update customers
                       set 
                       city = 'İstanbul'
                       where city = 'Adana' """
    connection.commit()
    connection.close()
    
# updateCustomer()         
def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" Delete from customers where customer id = 60 """
     connection.commit()
     connection.close()
# deleteCustomer()     
def joinoperations():
         
         connection = sqlite3.connect("chinook.db")
         cursor = connection.execute(""" select albums.Title,
                                     artists.Name from artists
                                     inner join albums
                                     on artists.ArtistId = albums.ArtistId """)
         for row in cursor:
             print("Title: "+ row[0] " Name: "+row[1])
             print("*******************")                                                                                                
         connection.close()
                 