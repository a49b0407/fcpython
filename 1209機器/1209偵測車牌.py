# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:24:36 2021

@author: USER
"""

import cv2
import numpy as np
img = cv2.imread("car4.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_LIST,
                                    cv2.CHAIN_APPROX_SIMPLE)
for area in contours:
    if cv2.contourArea(area)>100000 and cv2.contourArea(area)<131000:#選取車牌範圍
        print(cv2.contourArea(area))
        x,y,w,h=cv2.boundingRect(area)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)#畫線，自動擷取框
    
    
   #cv2.imshow('car1',thresh)
        cv2.imshow('img',img)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()





