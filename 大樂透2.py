# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:11:53 2021

@author: user
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