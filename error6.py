# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:25:30 2021

@author: user
"""
def mathdemo(n1,n2):
    try:
        result=divmod(n1,n2)#divmod==// %整數餘數
    except Exception as ex :
        print('錯誤:',ex)
    else:
        print('結果:',result)
    finally:
        print('計算完畢')
num1,num2=eval(input('輸入2個數子用逗點隔開:'))#eval迭帶因有逗號
mathdemo(num1,num2)












