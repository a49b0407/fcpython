# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:37:05 2021

@author: user
"""
class objectDemo:
 def __new__(kind,name):        #物件生成
  if name !='':                 #物件生成
     print('物件已建構')          #物件生成
     return object.__new__(kind)#物件生成
  else:
      print('物件未建構')
      return None
 def __init__(self,name): 
    print('物件初始化')
    print(name)
d=objectDemo('john')    
a=objectDemo('')  
    
  
    
  
    
  
    
  
    
  