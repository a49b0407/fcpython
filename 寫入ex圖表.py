# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:30:07 2021

@author: user
"""
import openpyxl
from openpyxl.chart import BarChart,Reference
wb = openpyxl.Workbook()
ws = wb.active
rows = [['','2020年','2021年'],['bmw',300,153],
       ['toyota',1500,700],['audi',730,415]]
for r in rows :
    ws.append(r)
chart = BarChart()#建立直方圖
chart.title = '汽車銷售圖'
chart.x_axis.title='品牌'
chart.y_axis.title='銷售量'
data = Reference(ws,min_col=2,max_col=3,min_row=1,
                 max_row=4)#控制rows行與列
chart.add_data(data,titles_from_data=True)
xtitle = Reference(ws,min_col=1,min_row=2,
                   max_row=4)
chart.set_categories(xtitle)
ws.add_chart(chart,'E1')
wb.save('demo4.xlsx')



