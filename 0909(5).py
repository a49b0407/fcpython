# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:27:13 2021

@author: USER
"""
import requests
from bs4 import BeautifulSoup
url = 'https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/foreign-exchange-rates'
data = requests.get(url)
data.encoding = 'UTF-8'
data = data.text
soup = BeautifulSoup(data,'html.parser')
rate = soup.find(id='inteTable1')
countryr = rate.find_all('tr',class_='tableContent-light')
for row in countryr :
    ds = row.find_all('td')
    
    for r in ds :
        print(r.text)
