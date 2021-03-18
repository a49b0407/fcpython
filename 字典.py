# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:02:45 2021

@author: user
"""
data={1:'apple',2:'banana'}
data2={'a':100,'b':'banana'}
data3=dict(a='apple',b='banana')
print(data[2])
print(data2['a'])
print(data3['a'])
print()
bike={
    "停車場型態": "公有免費停車場",
    "停車場代碼": "0000",
    "停車場名稱": "城平路外免費停車場",
    "停車場地址": "臺南市安平區安平漁港管理中心兩側",
    "即時車位": -1,
    "一般大型車": 40,
    "一般小型車": 315,
    "身障者小型車": 0,
    "婦幼者小型車": 0,
    "綠能小型車": 0,
    "一般機車": 0,
    "身障者機車": 0,
  }
print(bike["停車場型態"])
print(bike["停車場地址"])

stu={'john':89,'peter':93,'may':72}
print(stu['peter'])
stu['may']=92
print(stu)
stu['sue']=100
print(stu)
print(stu.get('john'))
print(stu.get('cherry'))#get找的道KEY直就用，找不到就NONE
print(stu.get('cherry',60))
print(stu.get('john',86))




