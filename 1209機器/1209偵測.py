# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:51:17 2021

@author: USER
"""
#色調
#blue==>[110,100,100]~[130,255,255]
#[H-10,100,100]~[H+10,255,255]
#green==>[50,100,100]~[70,255,255]
#red==>[0,100,100]~[10,255,255]
#0紅 30黃 60綠 90青色 120藍 150 品紅色
import cv2
img=cv2.imread('001.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarachy = cv2.findContours(thresh,cv2.RETR_TREE,#cv2.RETR_TREE樹狀等級結構
                      cv2.CHAIN_APPROX_SIMPLE)#找邊框 cv2.RETR_LIST_EXTERNAL找框
#https://vimsky.com/zh-tw/examples/detail/python-attribute-cv2.RETR_TREE.html
print(len(contours))
print(contours)