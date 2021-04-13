# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:25:31 2021

@author: user
"""
class myerror(Exception):
    def __init__(self,r):
        self.r=r
    def __str__(self):
        return'錯誤半徑{}'.format(self.r)










