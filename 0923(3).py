# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:51:55 2021

@author: USER
"""

from selenium import webdriver

import time

from bs4 import BeautifulSoup


webpath = 'c:\chromedriver.exe'

driver = webdriver.Chrome(webpath)


driver.implicitly_wait(3)

driver.get('https://tw.buy.yahoo.com/category/40057185')


height = 700
for i in range(20):
    driver.execute_script("window.scrollTo(0,{})".format(height))
    height += 700
    time.sleep(1)
    
    
soup = BeautifulSoup(driver.page_source,'html.parser')    

p = soup.find_all('li',class_='BaseGridItem__grid___2wuJ7 BaseGridItem__multipleImage___37M7b')


for row in p:
    print(row.find('a').get('href'))