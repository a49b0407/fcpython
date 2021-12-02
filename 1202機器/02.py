# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:12:13 2021

@author: USER
"""
import cv2
import numpy as np
img=np.zeros((10,10),dtype=np.uint8)
#print(img)
img[3,2]=255
img[5,7]=255
print(img)
cv2.imshow('gray',img)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()