# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:17:07 2021

@author: USER
"""
import cv2
img=cv2.imread('lena.png',0)
print(img)
t,thr=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#threshold 二質化已127為中間點，THRESH_TRUNC大於127的質為127小於不變
print(t)
print(thr)
cv2.imshow('img',img)
cv2.imshow('img2',thr)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()
