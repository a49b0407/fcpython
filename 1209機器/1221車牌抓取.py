# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 18:46:37 2021

@author: USER
"""
#pip install opencv-python
#pip install pytesseract
import cv2
import pytesseract

from PIL import Image

path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = path
binary_threshold=100
#二質化
spacing=0.95
img=cv2.imread('car2.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,threshold=cv2.threshold(gray,binary_threshold,
                255,cv2.THRESH_BINARY)#加_INV拿掉就是相反
#inv二質化白轉黑，黑轉白

cv2.imshow('gray',threshold)


white=list()
black=list()
height=threshold.shape[0]
width=threshold.shape[1]
print(height,width)#印出長寬

white_max=0
black_max=0
count=0
for i in range(width):#先掃900次
    w_count=0
    b_count=0
    for x in range(height):    
        if threshold[x][i]==255:
            w_count +=1
        else:
            b_count +=1
    white_max=max(white_max,w_count)#max全部抓出來看是白底還是黑底
    black_max=max(black_max,b_count)#0~502掃過去辨識
    
    white.append(w_count)
    black.append(b_count)
#print('白色最大:',white_max)
#print('黑色最大:',black_max)
#起始點白色0.05*208=10.4 圖片白色地方的數子>10.4的開始抓
#結束點黑色0.95*502=476.9 圖片黑色地方的數字>476.9的地方開始抓
isB = black_max > white_max
#print(isB)

def find_end(start):
    end=start +1
    for m in range(start+1,width-1):#+1是開始跟結束不能同點
        if (black[m] if isB else white[m])>(spacing*black_max if isB else spacing*white_max):

            end=m
            break
    #print('End:',end)
    return end
n=1
start=1
end=2
i=0
#車牌只抓到最後一個字，空白框不抓
while n < width-1:
    n+=1
    if (white[n] if isB else black[n])>((1-spacing)*white_max if isB else (1-spacing)*black_max):
        start = n
        end = find_end(start)
        n = end
        #print('黑色:',black[n])
        if end-start > 20:
            i +=1
            #print(start,end)
            photo = threshold[1:height,
                start-10:end+10]#+10 -10 讓截圖的剛好
            text = pytesseract.image_to_string(photo,lang='eng',config='--psm 10 -c tessedit_char_whitelist=0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
            
            print(text.strip())
            cv2.imwrite(str(i)+'.jpg',photo)#一個個拆出來存檔
            cv2.imshow('number',photo)
            cv2.waitKey()            
            cv2.destroyAllWindows()
            
            
            
            
            