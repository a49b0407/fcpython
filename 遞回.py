# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:27:30 2021

@author: user
"""
def fun(x):#遞回5階
 if x <=1:
  return 1
 else:
  return x*fun(x-1)
print(fun(5))
print('-------------------------------')
def gcd(n,m):
 if m ==0:
  return n
 else:
  return gcd(m,n%m)
print(gcd(30,310))
print('-------------------------------')
def exterfun(x,y):
 def innerfun(a,b):
  return divmod(a,b)#divmod a=商=取餘數
 return innerfun(x,y)
print(exterfun(25,7))







