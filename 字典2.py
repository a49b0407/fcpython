# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:04:44 2021

@author: user
"""
stu={'tom':90,'david':88}
stu['eric']=62
stu.update({'may':93,'sue':91})
print(stu)
print('依姓名排序:')
for key in sorted(stu):
 print('%-10s %d'%(key,stu[key]))#d10進至數字
#stu.pop('john')
print('依姓名遞減排序:')
for key in sorted(stu,reverse=True):
 print('%-10s %d'%(key,stu[key]))
stu.clear()
stu.update(cherry=70,jack=91)
print(stu)


          