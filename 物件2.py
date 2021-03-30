# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:37:04 2021

@author: user
"""
class Account(object):
 def __init__ (self,num,name,amount):#初始化
    self.number=num
    self.name=name
    self.balance=amount
 def deposite(self,money):
    self.balance +=money
 def withdraw(self,money):
     if self.balance >= money:
         self.balance -= money
ac=Account('123-456-789','john',1000)
ac.deposite(199)
print(ac.balance)

ac.withdraw(1)
print(ac.balance)
