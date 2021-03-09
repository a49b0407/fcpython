# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:55:54 2021

@author: user
"""
for a in range(1,4):
    print('a=',a)
    for b in range(1,3):
        print(b,end=',')
    print()
print('程式完筆')
print()

for i in range(2,10):
    for j in range(1,10):
     print(i,'*',j,'=',i*j,sep='',end='\t')
    print()