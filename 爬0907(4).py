# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 21:23:13 2021

@author: USER
"""

import requests
import xml.sax
class BusHandler(xml.sax.ContentHandler):
    def startElement(self,name,attrs):
        if name == 'Route':
            print('路線:',attrs['nameZh'])
            print('起終點:',attrs['ddesc'])
            
if __name__ == '__main__':           
           parser = xml.sax.make_parser()
           bus = BusHandler()
           parser.setContentHandler(bus)
           url = 'http://ibus.tbkc.gov.tw/xmlbus/StaticData/GetRoute.xml'
           data = requests.get(url)   
           data.encoding = 'UTF-8'           
           data = data.text
           fileName = 'bike.xml'
           with open(fileName,'w',encoding='UTF-8') as fobj :
                fobj.write(data)
           parser.parse(fileName)            
            
            
            
            
            
            
            