# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:59:50 2019

@author: desaisuk
"""

#pip install selenium
#pip install bs4
#download chrome driver from link http://chromedriver.chromium.org/

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen

username = "pickuplimes"
browser = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
browser.get('https://www.instagram.com/'+username+'/?hl=en')
Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

links=[]
source = browser.page_source
data=bs(source, 'html.parser')
body = data.find('body')
script = body.find('span')
for link in script.findAll('a'):
     if re.match("/p", link.get('href')):
        links.append('https://www.instagram.com'+link.get('href'))