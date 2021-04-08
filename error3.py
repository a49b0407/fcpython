# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:36:29 2021

@author: user
"""
data=[1,2,3]
try:
    print(1000/0)
    print(data[3])
except Exception as ex :#ERROR都抓
    print(ex)
print('程式執行完畢')









