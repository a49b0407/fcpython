# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:31:02 2021

@author: user
"""

m = 0
name = input('輸入餐點A,B,C:')
if name == 'A': 
  m = m+130
  print(m,'元')
if name == 'B':
  m = m+150
  B = input('是否加購Y/N:')
  if B == 'Y':
   m = m+50
   print(m,'元')
  elif B == 'N':
    print(m,'元')
if name == 'C': 
  m = m+200
  print(m,'元') 








