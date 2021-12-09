# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:14:17 2021

@author: USER
"""

import cv2
import numpy as np
img = cv2.imread("car4.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#轉灰
#以下高濕去雜質自適
blur=cv2.GaussianBlur(gray,(7,7),1)
thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
#-----------------AND
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_LIST,
                                    cv2.CHAIN_APPROX_SIMPLE)
for area in contours:
    if cv2.contourArea(area)>100000 and cv2.contourArea(area)<131000:#選取車牌範圍
        print(cv2.contourArea(area))
        x,y,w,h=cv2.boundingRect(area)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)#畫線，自動擷取框
        numbers = img[y:y+h,x:x+w]
        gray = cv2.cvtColor(numbers,cv2.COLOR_BGR2GRAY)#以下高濕去雜質
        blur = cv2.GaussianBlur(gray,(7,7),4)
        _,thresh=cv2.threshold(blur,100,255,cv2.THRESH_BINARY)#變色
    
        cv2.imshow('img1',img)
        cv2.imshow('img2',blur)
        cv2.imshow('img3',gray)
        cv2.imshow('img4',thresh)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()