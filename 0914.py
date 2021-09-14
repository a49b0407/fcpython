# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:41:24 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/PingTung/index.html'
data = requests.get(url)
data.encoding = 'UTF-8'
data = data.text
sp = BeautifulSoup(data,'html.parser')
allr = sp.find_all('div',class_='r-ent')
for row in allr:
    print(row.find('div',class_='date').text,end=' ')
    print('https://www.ptt.cc'+row.a.get('href'),end=' ')  
    print(row.a.text)
    