# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:43:25 2021

@author: user
"""
import csv
f='student.csv' #ex格式
with open(f,'a',newline='',encoding='UTF8') as fo:
    csvWriter=csv.writer(fo)
    csvWriter.writerow(['姓名','系別','性別'])
    csvWriter.writerow(['王小明','資工系','男'])
    csvWriter.writerow(['陳小麗','企管系','女'])





