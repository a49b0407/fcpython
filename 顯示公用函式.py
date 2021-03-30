# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:24:42 2021

@author: user
"""

def display():
 print('買2送1')
def area(w,h):
 return w*h
def total(*value):
 t=sum(value)
 return t
if __name__=='__main__':#顯示public
    print('main')
    display()