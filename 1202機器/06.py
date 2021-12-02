# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:32:01 2021

@author: USER
"""

import cv2
img=cv2.imread('lena.png')
face=img[241:383,235:352]
cv2.imshow('face',face)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()#關掉視窗