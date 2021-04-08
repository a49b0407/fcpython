# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:32:53 2021

@author: user
"""

data=[1,2,3]
try:
    print(10+'10')
    print(10/0)
    print(data[3])
except (IndexError) as ex:#分抓ERROR
    print(ex)
    print('a處理')
except (ZeroDivisionError)  as o:#分抓ERROR
    print(o)
    print('b處理')
except:
    print('其他')
print('程式執行完畢')