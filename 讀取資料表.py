# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:37:04 2021

@author: user
"""
import sqlite3
conn = sqlite3.connect('lcc.db')
sql="select * from bike"
result = conn.execute(sql)
data=list (result)
print(data)
for row in result:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    
    
conn.commit()
conn.close()















