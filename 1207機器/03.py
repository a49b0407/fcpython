# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:26:54 2021

@author: USER
"""
import cv2
img=cv2.imread('lena.png',0)
print(img)
t,thr=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#threshold 二質化已127為中間點，THRESH_TOZERO小於等於設定值(127)都為0，比127大不動，THRESH_TOZERO_INV相反
print(t)
print(thr)
cv2.imshow('img',img)
cv2.imshow('img2',thr)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()
