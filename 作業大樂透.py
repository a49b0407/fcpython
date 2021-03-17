# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:25:55 2021

@author: fb-5231
"""
import random
number=[0,0,0,0,0,0]
i=0
while number.count(0) !=0:
     n=random.randint(1,49)
     if number.count(n)==0:
         number[i]=n
         i +=1
print(number)
