# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:37:51 2021

@author: USER
"""
#https://github.com/opencv/opencv/tree/master/data/haarcascades專家寫好的辨識程式
import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#辨識人臉圖片語法
eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')#辨識眼睛

img=cv2.imread('peo3.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,3)#1.3是辨識範圍(準確度)3是驗證3次
print('找到:',len(faces),'張臉')

for (x,y,w,h) in faces:
    im=cv2.rectangle(img,(x,y),(x+w,y+h),#畫方框3是眶寬度
                     (0,0,255),3)#找出忍臉位置
    roi_gray = gray[y:y+h,x:x+w]
    roi_img = im[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray,1.2,3,minSize=(10,10))    
    for (x,y,w,h) in eyes:
        im=cv2.rectangle(roi_img,(x,y),(x+w,y+h),(0,0,255),3) #畫方框3是眶寬度   
    print('找到眼睛:',len(eyes),'顆')
    
cv2.imshow('faces',img)
cv2.waitKey()            
cv2.destroyAllWindows()