# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 21:31:10 2021

@author: USER
"""
#!pip install cvzone
#!pip install mediapipe
import cv2
from cvzone.FaceDetectionModule import FaceDetector
from google.colab.patches import cv2_imshow
img1=cv2.imread('peo1.jpg')
img2=cv2.imread('peo2.jpg')
img3=cv2.imread('peo3.jpg')
detector=FaceDetector()
peo1,box1=detector.findFaces(img1)
cv2_imshow(peo1)

#peo1 2 3 要上傳



