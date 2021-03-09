# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:56:50 2021

@author: user
"""
import random
ans=random.randint(1,100)
guess=0
while ans != guess :
 guess=int(input('輸入1-100'))
 if guess > ans:
     print('小一點')
 if guess < ans:
     print('大一點')
print('對了')

++






