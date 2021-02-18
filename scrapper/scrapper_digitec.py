# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:06:07 2021

@author: Marc
"""


import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime, date
import time
import os
import pandas as pd
import threading


def scrapper(url):

    hdr = {	'Host': 'www.digitec.ch',
    				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    				'Accept-Language': 'en-US,en;q=0.5',
    				'DNT': '1',
    				'Referer': 'https://www.digitec.ch/',
    				'Connection': 'keep-alive',
				    'Cache-Control': 'max-age=0'}

    response = requests.get(url, headers=hdr)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # read the raw metadata
    price_raw = soup.find_all("meta", property="product:price:amount")
    product_raw= soup.find_all("meta", property="og:title")
    

    # scrap raw data for wantet stuff
    try:
        product = product_raw[0]['content']
    except:
        print("Missing product")

    try:
        price = price_raw[0]['content']
    except:
        price = 0
        print("Missing price for: " + product)

    content = {
        "Product" : product,
        "Price" : price
        }
    
    return content
