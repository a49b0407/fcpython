# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 21:51:03 2021

@author: user
"""

import sqlite3
conn = sqlite3.connect('lcc.db')
sql="select customer.name,orders.prices from customer inner join orders on customer.cid=orders.cid"
result = conn.execute(sql)

for row in result:
    print(row[0])
    print(row[1])

    
    
conn.commit()
conn.close()