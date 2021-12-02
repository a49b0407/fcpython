# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:52:56 2021

@author: USER
"""

import cv2
import numpy as np
blue=np.zeros((300,300,3),dtype=np.uint8)
print(blue)
blue[:,:,0]=255
print(blue)
cv2.imshow('blue',blue)

red=np.zeros((300,300,3),dtype=np.uint8)

red[:,:,2]=255
print(red)
cv2.imshow('red',red)

green=np.zeros((300,300,3),dtype=np.uint8)

green[:,:,1]=255
print(green)
cv2.imshow('green',green)

other=np.zeros((300,300,3),dtype=np.uint8)
other[:,:,1]=255
other[:,:,2]=255
cv2.imshow('green',other)

cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()#關掉視窗
