# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:26:18 2021

@author: USER
"""
import requests

from bs4 import BeautifulSoup
with open ('school.csv','w',encoding=('UTF-8')) as fObj:
    fObj.write('學校,地址,電話,網址\n')
for i in range(1,9):
    
    url = 'https://highschool.yjvs.chc.edu.tw/search/index.php'#另一種抓法
    param = {'city':9}
    param['page']=i
    
    data = requests.get(url,params=param)
    data.encoding = 'UTF-8'
    data = data.text
    
    sp = BeautifulSoup(data,'html.parser')
    schools = sp.find(id='school-list').find_all('table')
    for row in schools :
        item = row.find_all('li')
        with open('school.csv','a',encoding=('UTF-8')) as f:#存到EX檔
            f.write('{},{},{},{}\n'.format(item[0].text,item[1].text,item[2].text,item[3].text))
       # print(item[0].text,item[1].text,item[2].text,item[3].text)
      
