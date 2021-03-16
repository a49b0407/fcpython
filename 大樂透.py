# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:03:40 2021

@author: user
"""
import random
number=list()
while len(number) !=6:
    n = random.randint(1,49)
    if number.count(n)==0:
         number.append(n)
print(number)
