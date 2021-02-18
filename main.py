# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:06:07 2021

@author: Marc
"""

"""
ToDo:
    swichcase for vendor / scrapper
    change wishlist to a df
        add product category

"""

from datetime import datetime, date
import time
import random

from scrapper import scrapper_digitec
import tools


path = "./data"


def workWishlist(csv):
    for count, url in enumerate(csv):
        # convert to string to get rid of the "list"
        url_string = ''.join(url)

        # find out what vendor the url belongs to
        vendor = tools.getVendor(url_string)
        
        # choose the scrapper according to the vendor
        if vendor == "digitec":    
            priceForProduct = scrapper_digitec.scrapper(url_string)
        
            # write to csv
            tools.csv_writer(priceForProduct, vendor)
            
        elif vendor == "microspot":
            pass
        
        print("Passed run for objekt Nr. " + str(count) + ": " + priceForProduct["Product"])

# Main function / lööp
while True:
    wishlist = tools.csv_reader(path + "/" + "wishlist.csv")
    print( "\n" + "time to wake up " + datetime.now().strftime("%H:%M:%S") + "\n")

    workWishlist(wishlist)

    print("Run finished, sleep now.")
    time.sleep(random.randint(50,75))
