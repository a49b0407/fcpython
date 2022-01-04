# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 18:53:58 2022

@author: USER
"""

import face_recognition
import pickle #把臉部資料存進去
import pymysql
conn = pymysql.connect(host="localhost",user="root",
 password="123456789",database="lcc",charset="utf8")#連線

cursor = conn.cursor()

know_img = face_recognition.load_image_file('saa.jpg')

face_encoding = face_recognition.face_encodings(know_img)[0]

face_data = pickle.dumps(face_encoding)#輸出圖片資料(臉部)

name = input('輸入名子:')

#sql='insert into face(name,face_encoding) values(%s,%s)', (name,face_data)

cursor.execute('insert into face(name,face_encoding) values(%s,%s)', (name,face_data))
conn.commit()#送出