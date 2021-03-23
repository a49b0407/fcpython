# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:05:05 2021

@author: user
"""
def total(start,stop,sep):
 t=0
 for i in range(start,stop,sep):
  t+=i
 return t
key=input('案y開始')
while key=='y':
 s=int(input('初始值:'))
 e=int(input('終止質'))
 p=int(input('開始值'))
 sum=total(s,e,p)
 print('總和:',sum)
 key=input('案y繼續')





