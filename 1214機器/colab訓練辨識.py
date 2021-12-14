# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 20:33:44 2021

@author: USER
"""

#colab
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
#訓練模組用
from tensorflow.keras.layers import Dense,Activation
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.datasets import mnist
#https://ithelp.ithome.com.tw/articles/10191725
(x_train,y_train)<(x_test,y_test)=mnist.load_data()
len(x_train)
len(x_test)
x_train.shape
x_train[0]
plt.imshow(x_train[0],cmap='binary')
y_train[0]
t1=x_train.reshape(60000,784)
x_train=x_train.reshape(60000,-1)#轉一維
x_test=x_test.reshape(10000,-1)
x_train.shape
t1.shape
x_train=x_train / 255
x_test = x_test / 255
y_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)#辨識種類
y_train[1]
model=Sequential()
model.add(Dense(20,input_dim=784,activation='relu'))#激勵涵式
#https://mropengate.blogspot.com/2017/02/deep-learning-role-of-activation.html
model.add(Dense(40,activation='relu'))#40數字越來越大神經元越大
model.add(Dense(80,activation='relu'))
model.add(Dense)(10,activation='softmax')#softmax分類用
model.compile(loss='mse',optimizer=SGD(learning_rate=0.05),#optimizer=SGD標準梯度升降 learning_rate學習數率0.05要校調
              metrics=['accuracy'])#loss遺失涵式 mse平均方差 accuracy正確率
model.summary()#顯示摘要
#15700 784*20+20
#840 20*40+40
model.fit(x_train,y_train,
    validation_batch_size=0.2,#比例
    batch_size=100,epochs=20)#100筆資料訓練20次
score=model.evaluate(x_test,y_test)
score#算分數
predict=model.predict(x_test)
ans=np.argmax(predict[0])
ans#辨識哪個最正確(最大)





