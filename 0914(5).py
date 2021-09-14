# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:48:55 2021

@author: USER
"""

import requests

from bs4 import BeautifulSoup
url = 'https://www.irasutoya.com/2021/01/onepiece.html'

data = requests.get(url)
data.encoding = 'UTF-8'
data = data.text
sp = BeautifulSoup(data,'html.parser')
allimg = sp.find_all('div',class_='floatimg')
i = 1
for row in allimg:
    filename = str(i) + '.png'
    img = row.img.get('src')
    pic = requests.get(img)
    with open(filename,'wb') as f:
        f.write(pic.content)
    i+=1
    #print(img)






