# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:36:13 2021

@author: USER
"""


import requests
import json

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

url ='https://covid19dashboard.cdc.gov.tw/dash2'

data = requests.get(url,headers=header)

data.encoding = 'UTF-8'

data = data.text

cov = json.loads(data)

GC = cov['0']

print('全球確診人數：',GC['cases'])
print('全球死亡人數：',GC['deaths'])



url ='https://covid19dashboard.cdc.gov.tw/dash3'

data = requests.get(url,headers=header)

data.encoding = 'UTF-8'

data = data.text

cov = json.loads(data)

GC = cov['0']

print('全球確診人數：',GC['確診'])
print('全球死亡人數：',GC['死亡'])
print('全球死亡人數：',GC['昨日確診'])





