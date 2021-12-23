# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 21:03:08 2021

@author: USER
"""

import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#辨識人臉圖片語法
eye_cascade=cv2.CascadeClassifier('haarcascade_mcs_nose.xml')#辨識眼睛

img=cv2.imread('img/facemask2.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,3)#1.3是辨識範圍(準確度)3是驗證3次
print('偵測到:',len(faces),'張')
count = 0
for (x,y,w,h) in faces:
    im=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)#畫方框3是眶寬度
                                                        #找出忍臉位置
    roi_gray = gray[y:y+h,x:x+w]
    roi_img = im[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray,1.2,3,minSize=(50,50))    
    for (x,y,w,h) in eyes:
        im=cv2.rectangle(roi_img,(x,y),(x+w,y+h),(0,0,255),3) #畫方框3是眶寬度   
        count +=1
        break        
        
        
    print('沒戴口罩:',count,'位')
    
cv2.imshow('faces',img)
cv2.waitKey()            
cv2.destroyAllWindows()