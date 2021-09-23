# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:39:35 2021

@author: USER
"""
import requests
from bs4 import BeautifulSoup

url = 'https://supertaste.tvbs.com.tw/food'

data = requests.get(url)
data.encoding = 'UTF-8'
data = data.text
soup = BeautifulSoup(data,'html.parser')

foods = soup.find(id = 'combolistUl')#找到整個的區塊

items = foods.find_all('li')#區塊裡面全部的li

for row in items:
    if len (row.find_all('a'))>0:
        link = row.find_all('a')[0].get('href')
        img = row.find('img').get('data-original')
        title = row.find('div',class_='txt').text
        print(img)
        print(title)
        print(link)