# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:37:04 2021

@author: user
"""
import sqlite3
conn = sqlite3.connect('lcc.db')#存在就連不存在就建
sql="create table if not exists customer(cid integer primary key autoincrement,name varchar(30),sex varchar(2))"#用雙引號包
conn.execute(sql)#執行語法
conn.commit()#提交即生效

sql="create table if not exists orders(id integer primary key autoincrement,prices int,cid int)"
conn.execute(sql)#執行語法
conn.commit()#提交即生效
conn.close()















