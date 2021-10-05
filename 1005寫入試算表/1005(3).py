# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:01:41 2021

@author: USER
"""
#讀取簡單圖片文字
import pytesseract
from PIL import Image

path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"#r絕對路徑
pytesseract.pytesseract.tesseract_cmd = path
img = Image.open(r"001.jpg")#檔名

text = pytesseract.image_to_string(img,lang='chi_tra')#讀取文字
print(text.strip())                  #數字用 'eng',config='--psm 10 -c tessedit_char_whitelist=0123456789' 
                                     #10是單一個字幅
