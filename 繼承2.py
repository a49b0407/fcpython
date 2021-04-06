# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:21:18 2021

@author: user
"""
class parent:
    def show1(self):
        print('parent show1')
    def show2(self):
        print('parent show2')
class son(parent):
    def display(self):
        print('son display')
class daughter(parent):        
    def show2(self):
        print('daughter show2')
    def display(self):
        print('daught display')
class   grandchild(son,daughter):
    def message(self):
        print('grandchild msg') 
tom=grandchild()
tom.message()
tom.display()
tom.show2()
tom.show1()