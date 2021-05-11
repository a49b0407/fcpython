# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:10:13 2021

@author: user
"""
import pandas as pd
data = pd.read_csv('tbike.csv')
print(data)

rate = pd.read_html("https://rate.bot.com.tw/xrt")
print(rate)

