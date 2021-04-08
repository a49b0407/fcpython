# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:10:19 2021

@author: user
"""
data=[1,2,3]
try:
    print(data[3])
    print(10/0)
    
except (IndexError,ZeroDivisionError) as ex:#錯誤捕獲
    print(ex)
    
print('程式執行完畢')    
    
    