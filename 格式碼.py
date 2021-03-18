# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:16:32 2021

@author: user
"""
name='peter'
pi=3.1415926
money=10000
print('學生:%s的存款%d元'%(name,money))
print('存款:%10d,目前利率:%10.2f'%(money,pi))
print('姓名:{},存款為{}元'.format(name,money))
print('利率:{0},金額:{1},pi:{0}'.format(pi,money))
print('存款:{:,},利率:{:.2f}'.format(money,pi))
print('存款:{0:10d},補0:{0:0>10d}'.format(money))
print('姓名:{:>10s}君'.format(name))
print('姓名:{:<10s}君'.format(name))


