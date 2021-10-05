# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:09:50 2021

@author: USER
"""

import gspread#憑證
from oauth2client.service_account import ServiceAccountCredentials#認證
import requests
import json

def auth_client(path,scopes):
    credintials =  ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
    return gspread.authorize(credintials)
    
path ='c://pythonexlce//pythonexlce-b7699dd8e87f.json'#google consol
scopes = ['https://spreadsheets.google.com/feeds']
client = auth_client(path,scopes)
key = '1xrf9G0OPebDjkWxHStEkUbLiBUjl28Fj0N2SfGXEImE'
ws = client.open_by_key(key)
#sheet = ws.get_worksheet(0)#用索引直抓
sheet = ws.worksheet('產品')#用工作表抓

#sheet.update_cell(3,6,'hello')#寫入
print(sheet.cell(8,3).value)#第8行地3列 8行C
print(sheet.cell(9,3).value)
print(sheet.cell(10,3).value)


