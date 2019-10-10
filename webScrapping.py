# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:27:57 2019

@author: desaisuk
"""

#pip install bs4
#pip install requests

import requests
import bs4


#Pass url 
res = requests.get('https://simplesite.com')

#type(res)
#res.text

#Convert it to bs4 object to parse
soup = bs4.BeautifulSoup(res.text, 'lxml')

#type(soup)

#give html tag names to extract data
ttl = soup.select('title')
ttl[0].getText()