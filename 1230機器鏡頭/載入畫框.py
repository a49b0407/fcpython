# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:40:14 2021

@author: USER
"""
#google colab
#!pip install cmake
#!pip install face-recognition

drive.mount('/content/drive') 掛載雲端硬碟
import face_recognition
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw
fileName='/content/drive/MyDrive/lcc/fcu/img2.jfif'
#圖片檔案路徑
image=face_recognition.load_image_file(fileName)
#叫出圖片檔案
box =face_recognition.face_locations(image)
#叫出圖片檔案的臉
print(box)
img=Image.open(fileName)
draw=ImageDraw.Draw(img)
for i in range(len(box)):
  draw.rectangle((box[i][3],box[i][0],box[i][1],box[i][2]),outline='red',
                 width=2)
plt.imshow(img)
plt.show




