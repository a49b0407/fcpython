# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:54:23 2021

@author: user
"""
fruits=['apple','banana','orange','apple','cherry','apple']
q=input('搜尋水果:')
if fruits.count(q)==0:
    print('找不到',q)
else:
    c=fruits.count(q)    #c=跑幾次
    ind=0                #ind=顯示所引值
    for i in range(c):
        n=fruits.index(q,ind)
        print(ind,'位置')
        ind+=1

