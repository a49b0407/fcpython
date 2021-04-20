# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:30:06 2021

@author: user
"""
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws['a1']='連成電腦'
rows=[['英文','數學','資訊'],[60,30,100],[50,98,81]]
for r in rows:
    ws.append(r)
wb.save('demo.xlsx')











