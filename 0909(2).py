# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:37:33 2021

@author: USER
"""
import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/index_new.aspx'
data = requests.get(url)
data.encoding = 'UTF-8'
data = data.text
sp = BeautifulSoup(data,'html.parser')
ball = sp.find('div',class_='ball_box01')
print(ball)
number = ball.find_all('div',class_='ball_tx ball_yellow')
for row in number :
     print(row.text,end=',')
print()


