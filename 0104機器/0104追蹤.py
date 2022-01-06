# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 20:27:11 2022

@author: USER
"""
#追蹤
import dlib
import cv2
def onMouseCliked(events,x,y,flags,param):
    global selection,track_window,drag_start
    if events == cv2.EVENT_LBUTTONDOWN:
#https://vimsky.com/zh-tw/examples/detail/python-attribute-cv2.EVENT_LBUTTONDOWN.html
        drag_start=(x,y)
        track_window = None
    if  drag_start:
        xMin = min(x,drag_start[0])    
        yMin = min(y,drag_start[1])
        xMax = max(x,drag_start[0])
        yMax = max(y,drag_start[1])
        
        selection=(xMin,yMin,xMax,yMax)
    if events == cv2.EVENT_LBUTTONUP:
        drag_start=None
        track_window = selection
        selection=None
 #https://ithelp.ithome.com.tw/articles/10212669       
tracker = dlib.correlation_tracker()
cap = cv2.VideoCapture(0)#打開相機        
drag_start=None
selection=None
track_window=None
start_flag=True

cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
#https://www.itread01.com/content/1544736979.html
cv2.setMouseCallback('image',onMouseCliked)
while True:
    _,frame=cap.read()#開始框
    if start_flag == True:
        while True:
            img_first=frame.copy()#矩形
            if track_window:
                cv2.rectangle(img_first,
                (track_window[0],track_window[1]),#最小拉到最大
                (track_window[2],track_window[3]),
                (0,0,255),1)
            elif selection:
                cv2.rectangle(img_first,
                    (selection[0],selection[1]),
                    (selection[2],selection[3]),
                    (0,0,255),1)
            cv2.imshow('image',img_first)
            
            if cv2.waitKey(5) == 13:
                break
        start_flag=False
        tracker.start_track(frame,dlib.rectangle(track_window[0],
                                         track_window[1],
                                         track_window[2],
                                         track_window[3]))
    else:
        tracker.update(frame)
        box = tracker.get_position()
        cv2.rectangle(frame,(int(box.left()),
                             int(box.top())),
                            (int(box.right()),
                             int(box.bottom())),(0,255,255),1)
        
    cv2.imshow('image',frame)
    if cv2.waitKey(5)==27:
        break            
cap.release()
cv2.destroyAllWindows()     
        
        
        
        
        
