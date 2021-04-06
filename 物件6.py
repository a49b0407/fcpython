# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:21:03 2021

@author: user
"""
class Motor:
    count=0
    def __init__(self):
        Motor.count +=1
    @classmethod  #類別的方法  
    def equip(cls,remp,seats):
        print('排氣量:{},座位數:{}'.format(remp,seats))
    @staticmethod#靜態方法
    def display():
        print('有',Motor.count,'個物件')
#類別物件方式呼叫
car=Motor()
hybird=Motor()
sym=Motor()

car.equip(1800,4)
hybird.equip(3000,5)
Motor.equip(150,2)
Motor.diaplay()






