# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:11:14 2021

@author: user
"""
class father :
    def display(self,name):
        self.name=name
        print('father name is',self.name)
class mother:
    def display(self,name):
        self.name=name
        print('mpther name is',self.name)
class child(father,mother):        
      pass
class son(father):
      pass
print(child.__name__,'類別,繼承=個父類')
for item in child.__bases__: #屬性動態紀錄
    print(item)
john=son()
john.display('bii')
print(son.__name__,'的父類')
print(son.__bases__)
son.__bases__=(mother,)
john.display('mary')

