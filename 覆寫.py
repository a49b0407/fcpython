# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:11:13 2021

@author: user
"""
class mother:
    def display(self,pay):
        self.price=pay
        if self.price>=50000:
            self.price*=0.8
        print(' ={}:.'.format(self.price))
class son(mother):#複寫父類別
    def display(self,pay):#複寫父類別
        self.price=pay
        super().display(pay)#SUPER呼叫使用父類的方法
        if self.price >=50000:
            self.price *=0.9
        print('9折{:,}'.format(self.price))
mary=mother()
john=son()
print('60000打8折',end='')
mary.display(60000)
print('50000打9折',end='')
john.display(50000)

