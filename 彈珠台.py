# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:20:14 2021

@author: fb-5231
"""


marbles = int(input('投入彈珠:'))
fraction = 0
if marbles == 1:
    fraction = fraction+6
elif marbles == 2:
    fraction = fraction+12
elif marbles == 3:
    fraction = fraction+18
elif marbles == 4:
    fraction = fraction+24
elif marbles == 5:
    fraction = fraction+30

import random
r2 = random.randint(1,4)
print(r2)
if r2 == 4:
    fraction = fraction*1
elif r2 == 3:
    fraction = fraction*1.5
elif r2 == 2:
    fraction = fraction*2
elif r2 == 1:
    fraction = fraction*2.5    
print(fraction,'張彩票')
