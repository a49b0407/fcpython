# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:11:10 2021

@author: user
"""
class motor:
    def __init__(self,name,price=65,capacity=1500):
        self.name=name
        self.price=price
        self.capacity=capacity
        
    def equip(self,award):
        self.price += award
    def __repr__(self):
        msg='{:85},售價:{:7.2f}萬,排氣量:{:,}'.format(self.name,self.price,self.capacity)
        return msg
class hybrid(motor):
    def equip(self,award,cell=2.18):
        motor.equip(self,award+cell)#呼叫MOTOE的方法
    def tinted(self,opr):
        if opr==1:
            return '尊貴藍'
        else:
            return '魅力紅'
stand=motor('standard')
toyota=motor('yaris',price=73.3,capacity=1798)
print(toyota,'不含環景')
toyota.equip(1.2)
tesla=hybrid('tesla',180)
tesla.equip(3.3)
print('tesla is',tesla.tinted(2))
print('--三種車款--')
for item in (stand,toyota,tesla):
    print(item)