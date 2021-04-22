# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:33:43 2021

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np 
with open ('yrborn.txt') as fp :
    populations=fp.readlines()
yrborn=dict()
for p in populations:
    yr,tl,boy,girl=p.split()#抓取資料4欄
    yrborn[yr]={'boy':int(boy),'girl':int(girl)}
ind=np.arange(len(yrborn))
yrlist = sorted(list(yrborn.keys()))
bp=list()
bp_b=list()
bp_g=list()
for yr in yrlist:
    boys = yrborn[yr]['boy']
    girls = yrborn[yr]['girl']
    bp.append(boys+girls)
    bp_b.append(boys)
    bp_g.append(girls)
plt.subplot(211)#控圖2=圖1=列1=正在處理第1個
plt.plot(bp)
plt.subplot(212)#2=正在處理第2個
plt.plot(bp_b)
plt.plot(bp_g)
plt.title('1986-2015(boy=girl)')
plt.show()