# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:25:04 2021

@author: fb-5231
"""

 #第二題用range印出 (2,4,6,8)
for i in range(1,9):
   if i/2==1:
       for a in range(1,9):
          if a/4==1:
             for b in range(1,9):
                if b/6==1:
                  for c in range(1,9): 
                      if c/8==1:
                       print('(',i,',',a,',',b,',',c,')')
   