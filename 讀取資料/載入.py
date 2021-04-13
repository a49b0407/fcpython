# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 21:00:52 2021

@author: user
"""
#f='yahoo.txt'#讀檔YAHOO的文字
#f_obj=open(f,encoding='UTF-8')
#data= f_obj.read()
#f_obj.close()
#print(data)
f='yahoo.txt'
with open(f,encoding='UTF-8')as f_obj:
   # data=f_obj.read()
   # print(data)
   # print(data.rstrip())#刪除末端自元(空白)
   #for line in f_obj:#足行讀取(段行)
   #    print(line)
   #    f_list=f_obj.readlines()#變串列
   #    print(f_list)
   #data=f_obj.read()    
   #new_data=data.replace('陳玉勳','小豬')#取代修改文字
   #print(new_data)    