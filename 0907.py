# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:03:04 2021

@author: USER
"""
import requests
import json
url = 'http://tbike-data.tainan.gov.tw/Service/StationStatus/Json'
data = requests.get(url).text
#print(data)
bike = json.loads(data)#轉json
#print(bike[1])
for row in bike :
    print('車站:',row['StationName'])
    print('地址:',row['Address'])
    print('可藉:',row['AvaliableBikeCount'])
    print('可停:',row['AvaliableSpaceCount'])
    print()
