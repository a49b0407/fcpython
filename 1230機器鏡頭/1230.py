# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 19:11:09 2021

@author: USER
"""
#pip install opencv-python
import face_recognition

import matplotlib.pyplot as plt
from PIL import Image,ImageDraw
fileName='ss.Jpg'

img=face_recognition.load_image_file(fileName)
landmarks = face_recognition.face_landmarks(img)
print(landmarks)

dim = Image.open(fileName)
drawimg = ImageDraw.Draw(dim)
for mark in landmarks:
    drawimg.line(mark['right_eye'],width=5)
    drawimg.line(mark['left_eye'],width=5,fill='red')
   # for feature in mark.keys():
    #    drawimg.line(mark[feature],width=5)
plt.imshow(dim)
plt.show


