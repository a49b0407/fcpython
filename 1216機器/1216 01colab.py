# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:37:35 2021

@author: USER
"""
#遺失函示
#https://docs.microsoft.com/zh-tw/sql/machine-learning/r/reference/microsoftml/loss?view=sql-server-ver15
!pip install tensorflow
import tensorflow
import numpy as np
x1=np.random.random((500,1))
x2=np.random.random((500,1))+1#500個浮點數 +1就是浮點數+1
x_train=np.concatenate((x1,x2))
y1=np.zeros((500,),dtype=int)
y2=np.ones((500,),dtype=int)
y_train=np.concatenate((y1,y2))
y_train
model=tensorflow.keras.models.Sequential([tensorflow.keras.layers.Dense(units=10,input_dim=1,
     activation=tensorflow.nn.relu),tensorflow.keras.layers.Dense(units=20,activation=tensorflow.nn.relu),
                     tensorflow.keras.layers.Dense(units=2,activation=tensorflow.nn.softmax)])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
#自己生的DATA測試
x_test=np.array([[0.34567],[0.899],[0.123],[1.63]])
y_test=np.array([0,0,0,1])
predict=model.predict(x_test)
x_test
y_test
predict
#神經元:有需多條神經一條一條，神經元拓展辨識拓展
#隱藏層:接續神經元下一層用(橋接)
#----------------------------------
#Adam=>Adaptive Moment Estimation=>
#結合3個優化器:Adagrad,RMSprop,Momentum
#----------------------------------
#損失函示LOSS:分類用因為目標值式分類格式，因是2維陣列，
#表示0或1，為了將整數目標值，轉為為分類目標值
#----------------------------------












