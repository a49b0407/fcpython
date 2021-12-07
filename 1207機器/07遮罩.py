# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:08:45 2021

@author: USER
"""
import cv2
import numpy as np
img=cv2.imread('flower.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#h是色相，s飽和度，v
green_mask=cv2.inRange(hsv,(36,0,0),(70,255,255))
yellow_mask=cv2.inRange(hsv,(26,43,0),(34,255,255))

green=np.uint8([[[255,0,0]]])

hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
#cv2.imshow('img',img)
#https://www.peko-step.com/tool/tfcolor.html
cv2.imshow('green',green_mask)
cv2.imshow('yellow',yellow_mask)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()