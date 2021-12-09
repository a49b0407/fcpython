# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:37:04 2021

@author: user
"""
import sqlite3
conn = sqlite3.connect('lcc.db')

sql = "insert into customer(name,sex) values('王曉明','男'),('陳小利','女'),('陳比爾','男')"
conn.execute(sql)#執行語法
conn.commit()
#https://docs.python.org/zh-tw/3/glossary.html#term-iterator


sql = "insert into orders(prices,cid) values(10000,1),(1999,1),(3000,3),(8999,3)"
conn.execute(sql)#執行語法
conn.commit()
conn.close()


















