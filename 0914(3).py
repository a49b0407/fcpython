# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:53:09 2021

@author: USER
"""
import requests

from bs4 import BeautifulSoup
for i in range(1,9):
    
    url = 'https://highschool.yjvs.chc.edu.tw/search/index.php?city=9&page='+str(i)#ity=9&page='+str(i)字串不能相加
    data = requests.get(url)
    data.encoding = 'UTF-8'
    data = data.text
    
sp = BeautifulSoup(data,'html.parser')
schools = sp.find(id='school-list').find_all('table')
for row in schools :
    item = row.find_all('li')
    print(item[0].text,item[1].text,item[2].text,item[3].text)










