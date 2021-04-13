# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:25:18 2021

@author: user
"""
def display(a,b):
    try:
        total=a/b
        print(total)
    except Exception as ex:
        print(ex)
        raise ex  #噴錯拋出
    finally:   #一定要做
        print('一定做')
        
if __name__ == '__name__':
    try:        
        display(10,5)
        display(10,0)
    except Exception as e:
        print('main',e)












