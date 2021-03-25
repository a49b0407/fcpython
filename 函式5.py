# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:27:30 2021

@author: user
"""
def student(**score):
 print('分數:',score)#賦予值
student(tom=92,may=100,david=97)
print('-----------------------------')
def student(name,**score):#印出字典格式
 print('姓名:',name)
 print('分數:',score)
student('tom',國文=92,數學=100,英文=97)
print('-----------------------------')
def school(year,*subject,**score):
 print('學期:',year)
 print('必修科目有:')
 for item in subject:
   print(item,end=',')
 print()
 for name in sorted(score):
   print('{0:8s}{1}'.format(name,score[name]))
   print('_'*30)
   low={k:v for k,v in score.items()  if v<60}
   print('不及格有{}人'.format(len(low)))
 print(low)
school(110,'數學','國文','英文',tohn=90,may=100,david=30,tow=20)







