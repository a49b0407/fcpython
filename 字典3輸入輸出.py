# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:35:03 2021

@author: user
"""
stu={'john':80,'tom':90,'sue':91}
print('john' in stu)
print('david' in stu)
print('------------------------')
fruits={}
while True:
 f=input('輸入找尋水果(q離開)')
 if f=='q':
   break
 if f in fruits:
   print('{}的價格:{}元'.format(f,fruits[f]))
 else:    
    price=int(input('輸入價格:'))
    fruits[f]=price
print(fruits)










