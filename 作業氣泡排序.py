# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:30:38 2021

@author: fb-5231
"""

data=[10,20,90,5,7,1]
n=len(data)
for i in range(n-1):
    for x in range(n-i-1):
        if data[x] > data[x+1]:
           data[x],data[x+1]=data[x+1],data[x]
print(data)          