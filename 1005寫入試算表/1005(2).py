# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:46:40 2021

@author: USER
"""
import gspread#憑證
from oauth2client.service_account import ServiceAccountCredentials#認證
import requests
from bs4 import BeautifulSoup

def auth_client(path,scopes):
    credintials =  ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
    return gspread.authorize(credintials)
    
path ='c://pythonexlce//pythonexlce-b7699dd8e87f.json'#google consol
scopes = ['https://spreadsheets.google.com/feeds']
client = auth_client(path,scopes)
key = '1xrf9G0OPebDjkWxHStEkUbLiBUjl28Fj0N2SfGXEImE'
ws = client.open_by_key(key)
#sheet = ws.get_worksheet(0)#用索引直抓
sheet = ws.worksheet('yahoo')#用工作表抓
yahoourl = 'https://tw.buy.yahoo.com/category/31501656'

data = requests.get(yahoourl)
data.encoding = 'UTF-8'

data=data.text
soup = BeautifulSoup(data,'html.parser')

goods = soup.find_all('li',class_='TopProducts_item2_1H_DK')
p=2
for row in goods:
    title = (row.find('span',class_='TopProducts_subPrice_2_PEQ')).text
    price = row.find('div',class_='TopProducts_title_35HZQ').text
    price = price.replace('$','').replace(',','')
    
    
    sheet.update_cell(p,1, title)
    sheet.update_cell(p,2,price) 
    p += 1 
