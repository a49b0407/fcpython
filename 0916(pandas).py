# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 19:53:16 2021

@author: USER
"""
import requests
import json
import pandas as pd
url = 'https://www.thsrc.com.tw/TimeTable/Search'
head = {
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'       
        }
param = {
    'SearchType': 'S',
'Lang': 'TW',
'StartStation': 'TaiZhong',
'EndStation': 'TaiPei',
'OutWardSearchDate': '2021/09/16',
'OutWardSearchTime': '20:00',
'ReturnSearchDate': '2021/09/16',
'ReturnSearchTime': '20:00'
    }
data = requests.post(url,data = param,headers=head)
data.encoding = 'UTF-8'
data = data.text

haghway = json.loads(data)
info = haghway['data']['DepartureTable']['TrainItem'] #json抓法

number = list()
starttime = list()
endtime = list()
tourtime = list()

for row in info:
    gotime = row['DepartureTime'] + ':00'#找出20點的車次時間
    qtime = '20:00:00'                   #37 38 40 刪除是全部時間
    
    if gotime >= qtime:
        number.append(row['TrainNumber'])
        starttime.append(row['DepartureTime'])
        endtime.append(row['DestinationTime'])
        tourtime.append(row['Duration'])

th = pd.DataFrame({'車次':number,'出發時間':starttime,'到達':endtime,
                  '旅行':tourtime},columns = ['車次','出發時間','到達','旅行'])
print(th)
