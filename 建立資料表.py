# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:36:54 2021

@author: user
"""
import sqlite3
conn = sqlite3.connect('lcc.db')#存在就連不存在就建
sql="create table if not exists bike(id integer primary key autoincrement,station varchar(30),rent int,space int)"#用雙引號包
conn.execute(sql)#執行語法
conn.commit()#提交即生效
conn.close()
















