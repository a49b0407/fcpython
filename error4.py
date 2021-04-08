# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:44:10 2021

@author: user
"""

def func(a,b):
    try:
        result=a/b
        print(result)
    except Exception as err:
        print(err) 
    finally:
            print('計算完畢')
func(100,5)
func(10,0)