# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 18:39:45 2021

@author: USER
"""
#抓取table資料
import requests

from bs4 import BeautifulSoup
url = 'https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation'

head ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
#user 複製網頁的
param = {
   ' _csrf':' b77c3b9f-fb9f-4815-b22e-21a33a548980',
'rideDate': '2021/09/16',
'station': '3300-臺中'
    }#網頁複製
data = requests.post(url,data=param,headers=head)
data.encoding = 'UTF-8'
data = data.text

sp = BeautifulSoup (data,'html.parser')

allstation = sp.find(id='tab1')
print('順')
qtime = input('輸入查詢時間(HH:MM)')
qtime += ':00'
stations = allstation.find_all('tr')
for row in stations :
    tds = row.find_all('td')
    if len(tds) > 1:   
        cartime = tds[1].text + ':00'
        if cartime >= qtime:
            
            print(tds[0].text.replace('\n',''))#replace('\n','')取代斷行
            print(tds[1].text)
            print(tds[2].text)
            print(tds[3].text.replace('\n',''))
            print('-'*30)
        
#allstation = sp.find(id='tab2')
#print('逆')
#stations = allstation.find_all('tr')
#for row in stations :
    #tds = row.find_all('td')
    #if len(tds) > 1:   
        #print(tds[0].text.replace('\n',''))#replace('\n','')取代斷行
       # print(tds[1].text)
        #print(tds[2].text)
        #print(tds[3].text.replace('\n',''))
        #print('-'*30)        
       
        
        
        
        
        
        
        
        
        