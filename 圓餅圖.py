# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:33:43 2021

@author: user
"""
import matplotlib.pyplot as plt
labels = ['食','依','住','行','育樂']
sizes=[5,12,20,10,3]#大小
colors = ['red','blue','yellow','green','purple']#顏色
explode=(0.1,0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,colors=colors
        ,labeldistance=1.1,autopct='%3.1f%%',shadow=True
        ,startangle=90,pctdistance=0.6)
plt.axis('equal')
plt.legend()
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"
plt.show





















