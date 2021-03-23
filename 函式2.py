# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:29:50 2021

@author: user
"""
money=99
def display():
 money=10
 print('函式money:',money)
display()
print('外部money:',money)
print('-----------------------------')
def go():
 global money#全域money
 money=11
 print('go的money:',money)
go()
print(money)