# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:37:04 2021

@author: user
"""
#刪除台南資料的ID刪除後不存在了
import sqlite3
conn = sqlite3.connect('lcc.db')
bid = int(input('輸入刪除ID:'))
sql = "delete from bike where id={}".format(bid) 
conn.execute(sql)
conn.commit()
conn.close()
















