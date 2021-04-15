# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:16:38 2021

@author: user
"""
#建mypython資料夾
import os
dir = 'mypython'
if os.path.exists(dir):
    print('存在')
else:    
    os.mkdir(dir)
#c曹建mypython資料夾
import os
dir = 'C:\\mypythob'
if os.path.exists(dir):
    print('存在')
else:    
    os.mkdir(dir)
#有錯誤
#import os
#newpath = os.path.join('C:\\mypython','lcc.txt')
#with open(newpath,'a',encoding='UTF8') as fo.write('連成電腦\n') fo:








