# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:33:42 2021

@author: user
"""
import matplotlib.pyplot as plt
benz = [3360,4120,5500]
bmw = [4000,3600,4500]
lexms = [5300,2000,2120]
seq = [2018,2019,2020]
plt.xticks(seq)
linebenz,=plt.plot(seq,benz,'-*',label='benz')#+,連貫
linebmw,=plt.plot(seq,bmw,'-o',label='bmw')
linelexms,=plt.plot(seq,lexms,'-^',label='lexms')
plt.legend(handles=[linebenz,linebmw,linelexms
],loc=0,bbox_to_anchor=(1,1))#圖例,best放到最好的位置可改成數子,bbox是把圖利放在外面
plt.title('Sales report',fontsize=28)
plt.xlabel('Year',fontsize=24)
plt.ylabel('Amout',fontsize=24)
plt.tick_params(axis='both',labelsize=14,color='red')
plt.show()
























