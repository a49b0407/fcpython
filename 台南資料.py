# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:37:04 2021

@author: user
"""
#http://tbike-data.tainan.gov.tw/Service/StationStatus/Json
import sqlite3
import requests
import json
url ="http://tbike-data.tainan.gov.tw/Service/StationStatus/Json"
conn = sqlite3.connect('lcc.db')
content = requests.get(url).text
data = json.loads(content)
for row in data:
    sql="select * from bike where station='{}'".format(row['StationName'])
    result = conn.execute(sql)
    conn.commit()
    if len(list(result))==0:
        sql = "insert into bike (station,rent,space) values('{}',{},'{}')".format(row['StationName'],row['AvaliableBikeCount'],row['AvaliableSpaceCount'])
        conn.execute(sql)
        conn.commit()
    else:#更新資料
        sql = "update bike set rent={},space={} where station='{}'".format(row['AvaliableBikeCount'],row['AvaliableSpaceCount'],row['StationName'])
conn.execute(sql)
conn.commit()
conn.close()





