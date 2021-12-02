# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:21:27 2021

@author: USER
"""
import numpy as np 
import cv2

img=np.zeros((300,300,3),dtype=np.uint8)
img[0:50,0:100,0]=255 
img[:,100:200,1]=255
img[:,200:300,2]=255
print(img)
cv2.imshow('img',img)

cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()#關掉視窗