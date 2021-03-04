# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:25:04 2021

@author: fb-5231
"""

 #第二題用range印出 2,4,6,8
a=0
b=0
c=0
d=0
for i in range(1,9):
     if i/2==0:
      i=a
     if i/4==0:
      i=b
     if i/6==0:
      i=c
     if i/8==0:
      i=d   
      print(a,b,c,d)