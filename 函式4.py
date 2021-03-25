# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:27:29 2021

@author: user
"""
def total(*value):#*名稱==串列
 t=0
 for i in value:
  t+=i  #+改成* t要等於1
 return t 
print(total())
print(total(10,20,30))
print(total(1,2,3,4,5,6,7,8,9,10))
print('--------------------------------')
def personal(name,dep,*score):
 print('學生:',name)
 print('系別:',dep)
 if len(score)==0:
     print('0,0')
 else:    
      total=sum(score)
      print('總分:{},平均:{}'.format(total,total/len(score)))
personal('john','math',90,80,55)
personal('peter','chinese')#第3個SCORE可為空，先卡的觀念
print('--------------------------------')
def school(name,*score,teacher):
 print('姓名:',name)
 print('總分:',sum(score))
 print('導師:',teacher)
school('john',60,70,88,80,teacher='peter')#tea是關鍵字不給會erroe
print('--------------------------------')
def student(name,*score,teacher='david'):
 print('姓名:',name)
 print('總分:',sum(score))
 print('導師:',teacher)
student('john',60,70,88,80,teacher='peter')
student('may',100,95,80)



