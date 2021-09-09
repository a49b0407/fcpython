# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:38:18 2021

@author: USER
"""
#parser HTML整理格式
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""
soup = BeautifulSoup(html_doc,'html.parser')
h2 = soup.find('h2')
p = soup.find('p')
print(h2.text)
print(p.text)
print()
h2_arr= soup.find_all('h2')
p_arr = soup.find_all('p')
print(h2_arr)
print(p_arr)
print()
a = soup.find('a')
a_text = a.text
href1 = a.get('href')
print(a_text)
print(href1)
print()
allink = soup.find_all('a')
for row in allink:
    txt = row.text
    link = row.get('href')
    print(txt)
    print(link)
