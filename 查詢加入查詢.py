# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:43:34 2021

@author: user
"""

student=['john','peter','may']
while True:
    q=input('輸入查詢性名:')
    if q=='q':
        break
    if student.count(q) !=0: #q有找到學生就印
        print('有學生:',q)
    else:    
        name=input('是否加入(Y/N):')
        if name =='y':
            student.append(q)
print('學生共有:',student)    