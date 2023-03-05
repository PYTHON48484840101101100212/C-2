# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 20:10:57 2023

@author: Coder
"""

import sqlite3

connection = sqlite3.connect("chinook.db")

# cursor = connection.execute("""" select FirstName,LastName from customers 
#                             where city = 'Prague' or city = 'Berlin'
#                             order by FirstName,LastName asc""") ##desc bunun ters sıralamasıdır!..

# for row in cursor:
#     print("FirstName: " + row[0])
#     print("LastName: " + row[1])
#     print("********************************************")
    
# connection.close() 

# cursor = connection.execute("""" select city,count(*) from Customers 
#                             group by city having count(*)>1 
#                             order by count(*) desc """) ##desc bunun ters sıralamasıdır!..

# for row in cursor:
#     print("City: " + row[0])
#     print("Count: " + str(row[1]))
#     print("********************************************")
    
# connection.close()   

cursor = connection.execute("""" select FirstName,LastName 
                            from customers 
                            where FirstName like '%a' """) ##desc bunun ters sıralamasıdır!..

for row in cursor:
    print("FirstName: " + row[0])
    print("LastName: " + row[1])
    print("********************************************")
    
connection.close() 