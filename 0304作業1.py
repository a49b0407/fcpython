# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:50:54 2021

@author: fb-5231
"""

#第一題計算1~50含50的和c是奇數和#sum是偶數和
sum=0
c=0
for i in range(1,51):
 if i %2 ==0:
     sum=sum+i
     print(sum)
 if i %2==1:
     c=c+i    
     print(c)
