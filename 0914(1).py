# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:11:10 2021

@author: USER
"""
import requests
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/PingTung/index.html'
for i in range(5):
    print('地{}頁'.format(i+1))    
    data = requests.get(url)
    data.encoding = 'UTF-8'
    data = data.text
    print('')
    sp = BeautifulSoup(data,'html.parser')
    allr = sp.find_all('div',class_='r-ent')
    for row in allr:
        print(row.find('div',class_='date').text,end=' ')
        print('https://www.ptt.cc'+row.a.get('href'),end=' ')  
        print(row.a.text)
    url = 'https://www.ptt.cc'+sp.find_all('a',class_='btn wide')[1].get('href')