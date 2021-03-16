# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:33:48 2021

@author: user
"""

#元組 Tuple 只能讀不能改
data=(10,'a',100,90)
print(type(data))
print(data[1])
new=list(data)  #轉換type改植
new[0]=100
olddata=tuple(new)
print(olddata)
num=1,2,3,4
print(num)


