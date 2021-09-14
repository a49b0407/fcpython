# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:35:15 2021

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



for row in allimg:
    img = row.img.get('src')
    filename = img.split('/')[-1]
      
   
    
    pic = requests.get(img)
    with open(filename,'wb') as f:
        f.write(pic.content)
   