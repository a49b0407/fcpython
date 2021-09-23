# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:38:38 2021

@author: USER
"""
from selenium import webdriver
import time
from bs4 import BeautifulSoup
webpath = 'c:\chromedriver.exe'
driver = webdriver.Chrome(webpath)
driver.implicitly_wait(3)
driver.get('https://supertaste.tvbs.com.tw/food')
#觸發網頁爬資料
for i in range(20):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')#
    time.sleep(1)
soup = BeautifulSoup(driver.page_source,'html.parser')    
foods = soup.find(id = 'combolistUl')#找到整個的區塊

items = foods.find_all('li')#區塊裡面全部的li

for row in items:
    if len (row.find_all('a'))>0:
        link = row.find_all('a')[0].get('href')
        img = row.find('img').get('data-original')
        title = row.find('div',class_='txt').text
        print(img)
        print(title)
        print(link)    