# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:41:04 2021

@author: USER
"""
import requests

import json
#pchome24H
url = 'https://24h.pchome.com.tw/cdn/onsale/v4/20210928/random/data.json&27213825'
data = requests.get(url)
data.encoding = 'UTF-8'
data = data.text
item = data.split('var')#在var做切割後是list
#json 格式破解VAR是多的
goods = item[1].strip()
index = goods.find('[{')
allgoods = goods[index:-1]
#print(allgoods)
infos = json.loads(allgoods)
for row in infos:
    goods = row['Nodes']
    for proj in goods:
        link = proj['Link']['Url']
        price = proj['Link']['Text']
        img = proj['Img']['Src']
        title = proj['Img']['Title']
        print(link)
        print(price)
        print(img)
        print(title)
        print('-'*50)