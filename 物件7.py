# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:11:13 2021

@author: user
"""
#self有關西要加無關西不加
class airplane :
    def __init__(self): #air呼叫此物件使用中華的名子
        self.name='中華'
    def fly(self):
        print('airplane:',self)
        print(self.name)
class boat:
    def __init__(self):#b呼叫此物件使用長榮的名子
        self.name='長榮'
    def swlm(self):
        print('boat:',self)
    def fly(self):
        airplane.fly(self)
        print(self.name)
air=airplane()
b=boat()
air.fly()
b.fly()









