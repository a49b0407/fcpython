# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:30:27 2021

@author: user
"""

import csv 
f='park.csv'
with open(f,encoding='UTF8') as fo:
    csvrReader = csv.reader(fo)
    listdata = list(csvrReader)
print(listdata)

for park in listdata:
    print(park[1])
    print(park[7])