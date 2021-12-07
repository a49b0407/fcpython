# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:21:20 2021

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

blur=cv2.medianBlur(img,3)
#區域

cv2.imshow('img',thr)
cv2.imshow('img2',blur)
cv2.imshow('Mean',athMean)
cv2.imshow('Gaus',athGaus)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()