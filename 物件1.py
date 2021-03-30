# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:37:04 2021

@author: user
"""
class Car():#定義類別
   def buildcar(self,name,color):
    self.name=name
    self.color=color
   def message(self):
    print('款式:{:6s},顏色:{:5s}'.format(self.name,self.color))
car=Car()
car.buildcar('小牛','黃蜂')
car.message()
car2=Car()
car2.buildcar('三陽','白')
car2.message()

