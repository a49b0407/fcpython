# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 19:43:21 2021

@author: USER
"""
#pip install opencv-python 
import  cv2
fileName="lena.png"
img=cv2.imread(fileName,0)#(,0)圖片轉灰
print(img.shape)
print(img)
cv2.imshow('img',img)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()#關掉視窗

