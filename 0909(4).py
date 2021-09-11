# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:17:05 2021

@author: USER
"""
import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/index_new.aspx'
data = requests.get(url)
data.encoding = 'UTF-8'
data = data.text
sp = BeautifulSoup(data, 'html.parser')
ball = sp.find_all('div', class_='contents_box02')
first = ball[0]
second = ball[2]

greens = first.find_all('div',class_='ball_tx ball_green')
red = first.find('div',class_='ball_red')

count = 0
for row in greens :
    if count > 5:
        print('特別號:',red.text)
yellow = second.find_all('div',class_='ball_tx_yellow') 
red = second.find('div',class_='ball_red')       
        
count = 0
for row in yellow:
    if count > 0:        
        print(row.text,end=',')
    count += 1
print('特別號:',red.text)    