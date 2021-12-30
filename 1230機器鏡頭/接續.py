# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 20:07:03 2021

@author: USER
"""
starName='/content/drive/MyDrive/lcc/fcu/hee.jpg'
starName2='/content/drive/MyDrive/lcc/fcu/hee1.jpg'
star1=face_recognition.load_image_file(starName)
star2=face_recognition.load_image_file(starName2)
#叫出圖片
know_face=face_recognition.face_encodings(star1)[0]
test_face=face_recognition.face_encodings(star2)[0]
face_distance=face_recognition.face_distance([know_face],test_face)
print(face_distance)
#圖片訓練比對相似度 128個特徵 [0]是第0個特徵
kf1='/content/drive/MyDrive/lcc/fcu/star1.jpg'
kf2='/content/drive/MyDrive/lcc/fcu/star3.jpg'
kf3='/content/drive/MyDrive/lcc/fcu/hee.jpg'
testf='/content/drive/MyDrive/lcc/fcu/wo.jpg'

kimg1=face_recognition.load_image_file(kf1)
kimg2=face_recognition.load_image_file(kf2)
kimg3=face_recognition.load_image_file(kf3)
timg1=face_recognition.load_image_file(testf)
know_name=['楊丞琳','貝莉梅','田馥甄','王心凌']

encoding1=face_recognition.face_encodings(kimg1)[0]
encoding2=face_recognition.face_encodings(kimg2)[0]
encoding3=face_recognition.face_encodings(kimg3)[0]
encoding4=face_recognition.face_encodings(timg1)[0]
know_faces=[encoding1,encoding2,encoding3]

result=face_recognition.compare_faces(know_faces,encoding4)
print(result)

face=''
for f in range(len(result)):
  if result[f]:
    face =face + know_names[f] + ","
if face=='':
  print('沒有符合的臉')
else:
  print(face)

import numpy as np
distance = face_recognition.face_distance(know_faces,encoding4)
print(distance)

index=np.argmin(distance)
if distance[index] < 0.4:
  print(know_names[index])
else:
  print('不符合')





