# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 21:21:06 2021

@author: USER
"""


import face_recognition
import cv2
import numpy as np
cap=cv2.VideoCapture(0)#鏡頭

hebe = face_recognition.load_image_file('ss.jpg')
hebeencod = face_recognition.face_encodings(hebe)[0]
wang=face_recognition.load_image_file('hee.jpg')
wangencod = face_recognition.face_encodings(wang)[0]

know_face = [hebeencod,wangencod]
know_name = ['balma','hebe']

face_locations=list()
face_encodings=list()
face_names=list()
while True:
    _,frame = cap.read()#開鏡頭
    small_frame = frame#cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_frame = small_frame[:,:,::-1]#bgr轉回來rgb
    face_locations=face_recognition.face_locations(rgb_frame)
    face_encodings=face_recognition.face_encodings(rgb_frame,
                                              face_locations)
    face_names=[]
    for face in face_encodings:
        distance = face_recognition.face_distance(know_face,
                                                       face)
        #print(know_face)
        index=np.argmin(distance)#找誰最小
        if distance[index] < 0.45 :
            name = know_name[index]
        else:
            name='UaKnow'
        face_names.append(name)
    for (top,right,bottom,left),name in zip(face_locations,
                                            face_names): 
        cv2.rectangle(frame,(left,top),(right,bottom),
                      (0,0,255),2)
        cv2.rectangle(frame,(left,bottom-35),(right,bottom),
                      (0,0,255),cv2.FILLED)

        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,name,
                    (left+6,bottom-6),font,1.0,(255,255,255),1)
        
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    
