# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:27:30 2021

@author: user
"""

def score(name,s1,s2,s3):
 print('學生:',name)
 print('分數:',s1,s2,s3)
 total=s1+s2+s3
 print('總分:',total)
number=[100,70,76]
score('john',*number)#可疊帶物件
print('-----------------------------------')
data={'x':80,'y':95,'z':100}#字典函式應用
def student(n1,n2,n3,x,y,z):
 print(n1,x)
 print(n2,y)
 print(n3,z)
student('john','mary','tom',**data)





























