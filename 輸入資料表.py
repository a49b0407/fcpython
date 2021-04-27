# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:37:03 2021

@author: user
"""
import sqlite3
conn = sqlite3.connect('lcc.db')
name = input('車站:')
rent = int(input('可借車位:'))
space = int(input('可停車位:'))
sql = "insert into bike(station,rent,space) values('{}',{},{})".format(name,rent,space)
conn.execute(sql)
conn.commit()
conn.close()














