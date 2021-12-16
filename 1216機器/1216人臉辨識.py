# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 21:28:52 2021

@author: USER
"""
!pip install face-recognition#人臉辨識
import face_recognition
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw
fileName=''
image=face_recognition.load_image_file(fileName)
box=face_recognition.face_locations(image)
box