# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:29:36 2021

@author: fb-5231
"""

import random
number=list()
while len(number) !=6:
    n = random.randint(1,49)
    if number.count(n)==0:
         number.append(n)
print(number)