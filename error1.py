# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:25:32 2021

@author: user
"""

data=[1,2,3]
try:
    print(10/0)
    print(data[3])
except (IndexError) as ex:
    print(ex)
    print('a處理')
except (ZeroDivisionError)  as o:
    print(o)
    print('b處理')
print('程式執行完畢')