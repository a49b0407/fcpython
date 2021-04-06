# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:21:14 2021

@author: user
"""
class Father:
    def car(self):
        print('Father car')
class mother:
    def house(self):
        print('Mother House')
class son(Father,mother):#繼承有順序性
    pass
s=son()
s.car()
s.house()





