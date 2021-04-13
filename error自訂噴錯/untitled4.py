# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:25:32 2021

@author: user
"""
import math
from CustomException import myerror
class Circle:
    def __init__(self,r):
        self.setR(r)
    def getR(self):
        return self.__r
    def setR(self,r):
        if r>0:
            self.__r=r
        else:
            raise myerror(r)
    def perm(self):
        return 2* self.__r* math.pi
    def area(self):
        return self.__r*self.__r*math.pi
    def __str__(self):
        return'圓周長:{:4.3f},園面積:{:4.3f}'.format(self.perm(),self.area())
try:
    one=Circle(12)
    print(one)
    two=Circle(-12)
    print(two)
except myerror as ex:
    print(ex)





