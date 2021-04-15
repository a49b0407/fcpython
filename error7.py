# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:16:38 2021

@author: user
"""
import datetime
def writelog(msg):  #時間
    now = datetime.datetime.now()
    strdate = now.strftime('%Y%m%d')
    strtime = now.strftime('%H:%M:%S')
    file=strdate+'.log'
    with open(file,'a',encoding='UTF8') as fo:
        fo.write(strtime+'\t')
        fo.write(msg+'\n')

try:#錯誤程式
    a = 10
    b = 0
   # print(a/b)
    data=[10,20,30]
    print(data[5])
except Exception as err:#記錄錯誤時間
    writelog(str(err))




