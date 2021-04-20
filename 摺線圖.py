# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:30:11 2021

@author: user
"""
import matplotlib.pyplot as plt 
data = [1,3,7,9,13,21,6]#線
data2 =[5,10,15,20,25,30]
plt.plot(data,linewidth=5,c='red')#摺線圖
plt.plot(data2)
plt.axis([0,6,0,30])#+刻度

plt.title('chart')
plt.xlabel('count')
plt.ylabel('value')
plt.show()







