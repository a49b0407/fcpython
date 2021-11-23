# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 21:30:51 2021

@author: USER
"""

import pyautogui
import time
print("畫圖 https://canvas.apps.chrome/")#畫布網址
time.sleep(5)
pyautogui.moreTo(x=500,y=550)
pyautogui.dragTo(x=1153,y=350,duration=3,button='left')
pyautogui.dragTo(x=1114,y=795,duration=3,button='left')
pyautogui.dragTo(x=500,y=550,duration=3,button='left')