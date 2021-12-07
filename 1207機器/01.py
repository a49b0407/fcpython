# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:50:52 2021

@author: USER
"""
import cv2
img=cv2.imread('lena.png')
t,thr=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#threshold 二質化已127為中間點，THRESH_BINARY是大於127的質為255小於為0
print(img)
print(thr)
cv2.imshow('img',img)
cv2.imshow('img2',thr)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()
