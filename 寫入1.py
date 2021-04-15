# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:05:19 2021

@author: user
"""

import csv
f= 'member.csv'
with open(f,'a',nweline='',encoding='UTF8') as fo:
    fields = ['姓名','性別','電話']
    dictWriter=csv.DictWriter(fo,fieldnames=fields)
    dictWriter.writeheader()
    dictWriter.writerow({'姓名':'王小明','性別':'女','電話':'0988987987'})
    
    
    
    
    