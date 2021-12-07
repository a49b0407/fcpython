# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:40:25 2021

@author: USER
"""
import cv2
img=cv2.imread('lena.png',0)
t,thr=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#以下程式只能處裡灰階圖
athMean=cv2.adaptiveThreshold(img,255,
                    cv2.ADAPTIVE_THRESH_MEAN_C,
                    cv2.THRESH_BINARY,5,3)
athGaus=cv2.adaptiveThreshold(img,255,
                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY,5,3)
#自適二級值ADAPTIVE_THRESH_MEAN是平均，THRESH_BINARY,5,3市矩形區域
#https://www.twblogs.net/a/5b8c1ba02b717718833082e1
#MEAN可換成GAUSSIAN是高濕模糊
cv2.imshow('img',thr)
cv2.imshow('Mean',athMean)
cv2.imshow('Gaus',athGaus)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()






