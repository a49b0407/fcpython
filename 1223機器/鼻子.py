# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 20:00:37 2021

@author: USER
"""
import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
nose_cascade=cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

img = cv2.imread('img/facemask5.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,3)

nose = nose_cascade.detectMultiScale(gray,1.3,maxSize=(50,50))
people=list()
#rectangle解說網址
#https://blog.gtwang.org/programming/opencv-drawing-functions-tutorial/
for (x,y,w,h) in nose:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#畫框
    #print('xywh:',len(nose))
    for (fx,fy,fw,fh) in faces:
        print('fx,fy,fw,fh',len(faces))
        if (fx+fw > x > fx and fy+fh > y > fy and fx not in people):#抓鼻子的位置
            people.append(fx)
            cv2.rectangle(img,(fx,fy),(fx+fw,fy+fh),(0,0,255),3)
        
        elif (fx in people):
            break
        else:
            cv2.rectangle(img,(fx,fy),(fx+fw,fy+fh),(255,255,0),3)
            
cv2.imshow('001',img)
cv2.waitKey()            
cv2.destroyAllWindows()           
            
    
            
            
            
            
            
            
            