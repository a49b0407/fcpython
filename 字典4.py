# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:35:03 2021

@author: user
"""
stu={'john':90,'tom':100,'may':92}
key=stu.keys()
value=stu.values()
item=stu.items()
print(key)
print(value)
print(item)
print('------------------------------')
listk=list(key)
listv=list(value)
listi=list(item)
print(listk,listv)
for i in range(len(listk)):
   print(listk[i],listv[i])
print('-----------------------------')
for k,v in listi :
   print(k,v)#24~26字典生成式
score={'tom':90,'david':70,'peter':30,'john':59,'mary':81,'may':93,'sue':60}  
print('大於70分有:',{k:v for k,v in score.items() if v>=70})
print('小於60分有:',{k:v for k,v in score.items() if v<60})
print('-----------------------------')   
data={}
for k,v in score.items():
 s=v//10
 if s not in data :
  data[s]=[]
 data[s].append(k)
print(data)
print('------------------------------')
for key in data.items():#判斷字典有無串列
   if isinstance(key,list):
    for value in key:
     print(value)
   else:  
     print(key)
  
     
     
     
     
     
     
     
     
     
     
     
     