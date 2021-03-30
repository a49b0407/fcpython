# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:37:05 2021

@author: user
"""
import math
class Circle:
    def __init__(self,r=5):
        self.r=r
    def  area(self):
         return self.r*self.r*math.pi 
    def perimeter(self):
        return 2*self.r*math.pi
fc=Circle()
print(fc.area())
print(fc.perimeter())
sc=Circle(15)
print(sc.area())
print(sc.perimeter())

