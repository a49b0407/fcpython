# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 20:47:34 2021

@author: USER
"""
import requests
from bs4 import BeautifulSoup

url = 'https://shopee.tw/search?keyword=switch'
header = {'cookie':'Googlebot','user-agent':'Googlebot'}

data = requests.get(url,headers=header)

data.encoding = 'UTF-8'
data = data.text

sp = BeautifulSoup(data,'html.parser')
items = sp.find_all('div',class_='col-xs-2-4 shopee-search-item-result__item')
for row in items:
    link = row.a.get('href')
    title = row.find('div',class_='_10Wbs- _5SSWfi UjjMrh')
    prices = row.find_all('span',class_='_1d9_77')
    if len(prices) == 1:
           print(prices[0].text)
    else:
        print(prices[0].etxt)
    print(title)
    print(link)
    print('-'*60)        
    
