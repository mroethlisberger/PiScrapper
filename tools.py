# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:06:07 2021

@author: Marc
"""

"""
ToDo:
    innterrupt code at any time
    that gay "
    maybe excell can stop beeing a bitch?
    sort by vendor into folders
    swichcase for vendor / scrapper
"""

import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime, date
import time
import os
import pandas as pd
import threading

from scrapper import scrapper_digitec

# def chooseScrapper(url):
#     switcher = {
#         "digitec": return scrapperDigitec(url)
#         }

path = "./data"

def checkFolder(path):
    if not os.path.isdir(path):
            try:  
                os.mkdir(path)
                print("Datafolder did not exist, create new one")
                return True

            except:
                print("ERROR: Cant create data folder.")
                return False
    else:
        return True

def csv_reader(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ";")
        data = list(reader)
        # print(data)

        return data

def csv_writer(obj, vendor):
    global path

    # check wheter data folder exist or not
    if not checkFolder(path):
        return False

    # create vendor folder
    try:
        os.mkdir(path + "/" + vendor)
    except OSError as e:
        # print("Directory exists")
        pass
        
    # create string with 
    filePath = path + "/" + vendor + "/" + obj["Product"] + ".csv"
    
    # get rid of the quotes
    filePath = awayWithTheGay(filePath)
    
    # data to write to the csv
    price = obj["Price"]
    today = date.today().strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # check wheter product file exists, append if true
    try:
        if os.path.isfile(filePath):
            # print("File did exist, yaaas")
            with open(filePath,'a') as f:
               writer = csv.writer(f)
               writer.writerow([today, current_time, price])
           
        else:
            print("File did not exist, create new one")
            with open (filePath, "w") as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Time", "Price"])
                writer.writerow([today, current_time, price])
                f.close()
                
    except:
            print("whoops")

def getVendor(url_string):
    first = url_string.find(".")
    second = url_string.find(".", first+1)

    vendor = url_string[first+1:second]
        
    # print(vendor)
    return vendor 

def awayWithTheGay(s):
    s = s.replace('"'," ")
    return s
