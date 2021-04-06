# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:20:47 2021

@author: user
"""
class Account:
 bank='聯成銀行'#類別變數
 count=0
 def __init__(self,number,name,balance):
  self.__number=number#__變數私人化
  self.__name=name
  self.__balance=balance
  Account.count +=1
 def deposite(self,money):
   if money>0:
     self.__balance += money
   else:
    raise ValueError('質不可小於0')#Valueerror內建錯誤
 def withDraw(self,money):
   if money>0:
     if self.__balance>=money:
       self.__balance-=money
 def getBalance(self):      
     return self.__balance 
 def __str__(self):#物件格式化      
     msg='帳號:{},戶名:{},餘額:{:,}'.format(self.__number,self.__name,self.__balance)  
     return msg
 def __repr__(self):
  return '給開發者看'    
 def __diplay(self):
  print('方法私人化')    
 def goRun(self):
     self.__display()



ac=Account('123-456','john',1000)
money= int(input('input money:'))
if  money>0:
     ac.deposite(money)
else:
    print('負數不可存')  

ac2=Account('456-789','perer',2000)
ac.deposite(5000)
ac.withDraw(2000)
print(ac.getBalance())
ac2.deposite(1000)#-1000 ERROR可用IF防範
print(ac2.getBalance())
print(ac2.bank)
Account.bank='聯邦銀行'
print(ac2.bank)
print(Account.count)
print(ac)
print(repr(ac))















