# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:33:42 2021

@author: user
"""
import matplotlib.pyplot as plt 
import numpy as np
name = 100
while True:
    x=np.random.random(100)
    y=np.random.random(100)
    color=['r','g','b','y','k']
    plt.scatter(x,y,s=100,c=x,cmap='brg')
    plt.show()
    key= input('plt input y:')
    if key !='y':
        break


















