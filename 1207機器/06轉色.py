# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:48:37 2021

@author: USER
"""

import cv2
import numpy as np
img=np.random.randint(0,255,size=[200,200],dtype=np.uint8)
img2=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print(img)
print('-'*35)
print(img2)
cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()





