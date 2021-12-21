# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:04:29 2021

@author: USER
"""

import pytesseract

from PIL import Image

path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = path

img = Image.open(r"007.jpg")

text = pytesseract.image_to_string(img,lang='eng',config='--psm 8 -c tessedit_char_whitelist=0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')

print(text.strip())