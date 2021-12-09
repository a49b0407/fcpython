# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 19:33:18 2021

@author: USER
"""

import cv2
import numpy as np
img=cv2.imread('001.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarachy = cv2.findContours(thresh,cv2.RETR_LIST,#cv2.RETR_TREE樹狀等級結構
                      cv2.CHAIN_APPROX_SIMPLE)#找邊框 cv2.RETR_LIST_EXTERNAL找框
#https://vimsky.com/zh-tw/examples/detail/python-attribute-cv2.RETR_TREE.html
print(len(contours))
print(contours[0])

print(contours[0].shape)
print(contours[1].shape)

for area in range(len(contours)):
    a = cv2.contourArea(contours[area])
    if a <= 30000:
        x,y,w,h=cv2.boundingRect(contours[area])
        print(x)
        print(y)
        print(w)
        print(h)        
        roi=np.array([[[x,y]],[[x+w,y]],[[x+w,y+h]],[[x,y+h]]])
        print(roi)
        #cv2.drawContours(img,[roi],-1,(0,0,255),3)
        #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        #cv2.drawContours(img,contours,area,(0,0,255),3)#畫邊框 3是邊框寬度
        cv2.imshow('img',img)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()
#https://yanwei-liu.medium.com/python%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E7%AD%86%E8%A8%98-%E4%B8%80-%E4%BD%BF%E7%94%A8open-cv%E8%BE%A8%E8%AD%98%E5%9C%96%E7%89%87%E5%8F%8A%E5%BD%B1%E7%89%87%E4%B8%AD%E7%9A%84%E4%BA%BA%E8%87%89-527ef48f3a86