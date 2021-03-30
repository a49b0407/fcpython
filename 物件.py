# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:37:02 2021

@author: user
"""
class clothes:
    def fly(self):#def==方法
        print('穿了會帥喔!')
    def show(self):
        print('台製')
        print('有機棉')
    def setName(self,name):#name與14行不同    
        self.name=name
c=clothes()
c.fly()
c.show()
c.setName('Nike')

c2=clothes()
c.setName('H&M')
print(c.name)
print(c2.name)






