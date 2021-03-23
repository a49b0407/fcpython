# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:35:04 2021

@author: user
"""
fruits={'apple':80,'banana':30,'orange':50}
n=fruits.setdefault('banana')
print(n)
n=fruits.setdefault('orange',150)
print(n)
n=fruits.setdefault('cherry',300)
print(n)
n=fruits.setdefault('cherry',400)
print(n)
print(fruits)











