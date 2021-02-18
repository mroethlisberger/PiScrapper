# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:39:24 2021

@author: Marc
"""

import requests
from bs4 import BeautifulSoup


url = "https://www.microspot.ch/de/mobiltelefon-tablet-wearables/tablet-ebook/tablets--c512000/apple-ipad-pro-2020-wifi-11-128-gb-space-grau--p0002346784"


hdr = {	'Host': 'www.microspot.ch',
				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'DNT': '1',
				'Referer': 'https://www.microspot.ch/',
				'Connection': 'keep-alive',
				    'Cache-Control': 'max-age=0'}

# make a soup :)
response = requests.get(url, headers=hdr)
soup = BeautifulSoup(response.text, 'html.parser')

# read the raw metadata
price  = soup.find_all('span', id="container-95e77350-5f09-11eb-a717-f93efced9f28-price")
print(price)

# tags = soup('span')
# for tag in tags:
#     print("this is the tag: " + str(tag) + " this is the content: " + str(tag.contents[0]))

