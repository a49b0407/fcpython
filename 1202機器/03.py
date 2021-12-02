# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:29:02 2021

@author: USER
"""
import  cv2
fileName="lena.png"
img=cv2.imread(fileName)#(,0)圖片轉灰

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
for x in range(100,200):
    for y in range(100,200):
        gray[x,y]=255


cv2.imshow('gray',gray)
cv2.waitKey()#等待按任何鍵
cv2.destroyAllWindows()#關掉視窗