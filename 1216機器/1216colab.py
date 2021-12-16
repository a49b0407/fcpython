# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:28:50 2021

@author: USER
"""
#接續1214
model.save('/content/drive/MyDrive/fcu/number.h5')
#https://sites.google.com/a/vtsh.tc.edu.tw/wei-dao-zhong-xue-cheng-shi-jing-ying-ban/tensorflow/wenzhangshengchengqi
!pip install gradio
import gradio as gr
import tensorflow
model = tensorflow.keras.models.load_model('/content/drive/MyDrive/fcu/number.h5')
def mnist(image):
  image=image.reshape(1,784)#784因為本來就是784所以給784
  prediction=model.predict(image).tolist()[0]
  return {str(i): prediction[i] for i in range(10)}
grobj=gr.Interface(fn=mnist,inputs='sketchpad',
        outputs=gr.outputs.Label(num_top_classes=3,label='預測結果'),title='手寫數字')#3是辨識3層
grobj.launch()#辨識語法辨識數字






