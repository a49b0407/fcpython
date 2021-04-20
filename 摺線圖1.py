# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:43:24 2021

@author: user
"""
import matplotlib.pyplot as plt 
data1=[1,2,3,4,5,6,7,8]
data2=[30,70,20,10,7,10,30,60]
data3=[2,7,9,8,14,17,6,20]
data4=[40,20,30,15,25,10,17,26]
seq=[1,2,3,4,8,6,7,8]#線的數量
plt.plot(seq,data1,'g--',seq,data2,'r-.',#--=虛線
         seq,data3,'y:',seq,data4,'k.')#:==點線
plt.title('chart',fontsize=30)
plt.xlabel('value',fontsize=18)
plt.ylabel('y_value',fontsize=18)