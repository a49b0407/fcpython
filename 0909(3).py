# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:06:16 2021

@author: USER
"""
import requests
from bs4 import BeautifulSoup
url = 'https://www.setn.com/ViewAll.aspx?PageGroupID=0'
data = requests.get(url)
data.encoding = 'UTF-8'
data = data.text
sp = BeautifulSoup(data,'html.parser')
allnews = sp.find_all('div',class_='col-sm-12 newsItems')
for row in allnews:
    t = row.find('time').text
    h3 = row.find('h3')
    title = row.find('a').text
    link = h3.find('a').get('href')
    print(title) 
    print(link)
    print(t)