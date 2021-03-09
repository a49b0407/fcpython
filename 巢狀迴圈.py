# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:50:18 2021

@author: user
"""

num = int (input('請輸入數子'))
for i in range(1,num+1):
    prime = 0
    for x in range(2,i):
        if i%x ==0:
            prime=1
    if prime ==0:
        print(i,'是質數')