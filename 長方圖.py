# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:33:42 2021

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
vote = [1600,900,1459]
n=len(vote)
x=np.arange(n)
width=0.4
plt.bar(x,vote,width)
plt.ylabel('numbers')
plt.xlabel('name')
plt.xticks(x,('john,peter','tom'))
plt.yticks(np.arange(0,2000,100))
plt.show()















