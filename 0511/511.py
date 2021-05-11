# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:10:10 2021

@author: user
"""
import pandas as pd
data = pd.Series([10,15,20,25,50])
print(data)

score = pd.Series([61,30,90,82],index=['john',
            'tom','mary','david'])#自定索引
print(score)
member = {'name':['王大明','陳水木','林森森'],'email':['wang@gmail.com',
        'chang@gmail.com','lin@gmail.com'],'tel':['0911334455',
        '0987987987','0978978978']}
member_pd = pd.DataFrame(member)
print(member_pd)
print(member_pd.info())#印出型別
print(member_pd.describe())#印出資訊





