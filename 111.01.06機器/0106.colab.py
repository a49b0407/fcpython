# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 19:38:36 2022

@author: USER
"""
#!pip install cvzone==1.3.7
#!pip install mediapipe==0.8.6
import cv2,math
from google.colab.patches import cv2_imshow
from cvzone.HandTrackingModule import HandDetector#手的追蹤
dH,dW=480,380
def resizeimg(image):
  h,w=image.shape[:2]
  if h<w:
    img=cv2.resize(image,(dW,math.floor(h/(w/dW))))#有小數點無條件捨去，負數就進位
  else:
    img=cv2.resize(image,(math.floor(w/(h/dH)),dH))
  return img   



img=resizeimg(cv2.imread('/content/drive/MyDrive/lcc/fcu/hand1.jpg'))
detector=HandDetector(mode=False,maxHands=2)#動態追蹤True
img1=detector.findHands(img)
cv2_imshow(img)

myHandType=detector.handType
print(myHandType)

ImList,bboxInfo=detector.findPosition(img)
print(ImList)
print(bboxInfo)

from cvzone.PoseModule import PoseDetector
img=resizeimg(cv2.imread('/content/drive/MyDrive/lcc/fcu/pose1.jpg'))
pose=PoseDetector()
img=pose.findPose(img)
cv2_imshow(img)


