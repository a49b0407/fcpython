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
ball = sp.find('div', class_='contents_box02')
first = allitem[0]
second = allitem[2]

greens = first.find_all('div',class_='ball_tx ball_green')
red = first.find('div')
