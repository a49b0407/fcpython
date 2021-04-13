# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:25:32 2021

@author: user
"""
data=[62,31,90,-1]
def demo(data):
    total=0
    for item in data:
        assert item>0,'輸入植要大於0'     #assert==斷言>0
        total += item
    return total
print('總和',demo(data))













