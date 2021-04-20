# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:30:07 2021

@author: user
"""
import openpyxl
wb = openpyxl.load_workbook('demo3.xlsx')#開啟demo3續寫


ws = wb.active#預設是sheet

title=['姓名','科系']
ws.append(title)
while True:
    stu=list()
    name=input('學生姓名:')
    if name == '':
        break
    dep=input('科系:')
    stu.append(name)
    stu.append(dep)
    ws.append(stu)
wb.save('demo3.xlsx')


















