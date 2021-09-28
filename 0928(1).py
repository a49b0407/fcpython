# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:43:34 2021

@author: USER
"""
import requests

import json
#kkday 澎湖
url = 'https://www.kkday.com/zh-tw/product/ajax_get_top_products?areaCode=A01-001-00019&upLimit=10&csrf_token_name=5b9b272fe2b1e1ce382771253cbbdf26'
data = requests.get(url)

data.encoding = 'UTF-8'
data = data.text
item = json.loads(data)
allit = item['data']
for row in allit:
    title = row['name']
    info = row['introduction']
    aaa = row['img_url']
    bbb = row['price']
    print(title)
    print(info)
    print(aaa)
    print(bbb)
    