# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:16:39 2021

@author: user
"""
import csv 
f='park.csv'
with open(f,encoding='UTF8') as fo:
    dictReader=csv.DictReader(fo)
    for row in dictReader:
        print(row)













