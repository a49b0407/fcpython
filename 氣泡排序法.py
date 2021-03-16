# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:20:28 2021

@author: user
"""
data=[10,20,90,5,7,1]
n=len(data)
for i in range(n-1):
    for x in range(n-i-1):
        if data[x] > data[x+1]:
           data[x],data[x+1]=data[x+1],data[x]
print(data)           