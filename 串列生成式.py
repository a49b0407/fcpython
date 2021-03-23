# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:35:03 2021

@author: user
"""
#兩個FOR相同意思，1~10放到串列
d=[]
for i in range(10):
 d.append(i)
print(d)
print('-'*45)
print([x for x in range(10)])
print('-'*45)
r=[]
for i in range(1,11):
 if i%2==0:
  r.append(i)
print(r)
print([i for i in range(1,11) if i%2==0])
print('-'*45)
score=[100,60,30,59,70,41,80]
s=[s for score if score>=60]
print








