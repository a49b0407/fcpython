# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:16:48 2021

@author: user
"""
import csv 
f='park.csv'
with open(f,encoding='UTF8') as fo:
    csvReader = csv.reader(fo)
    for item in csvReader:
        print('Row %s ='% csvReader.line_num,item)




















