# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:11:14 2021

@author: user
"""
class parent:
    def __init__(self):
        print('i am parent')
class child(parent):
    def __init__(self,name):#11行沒有就不會印13行
        super().__init__()
        print(name,'is child')
john=child('john')       
        
        
        
        
        