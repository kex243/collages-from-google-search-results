# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
from GoogleImageScrapper import GoogleImageScraper, GoogleImageScraperReverseSearch
import os, os.path
import csv


if __name__ == "__main__":
    
    with open(str("dictionary.csv"),encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        dictionary_of_elements = dict(reader)
    print (dictionary_of_elements)

    #Define file path
    webdriver_path = os.path.normpath(os.getcwd()+"\\webdriver\\chromedriver.exe")
    image_path = os.path.normpath(os.getcwd()+"\\photos")

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    # search_keys= ['apple','t-shirt']
    
    search_keys = list(str(dictionary_of_elements.get("keywords")).replace('quotsign','"').split(";"))

    #Parameters
    number_of_images = int(dictionary_of_elements.get("number_of_images_to_download"))
    headless = False
    min_resolution=(int(dictionary_of_elements.get("download_size_MinW")),int(dictionary_of_elements.get("download_size_MinH")))
    max_resolution=(int(dictionary_of_elements.get("download_size_MaxW")),int(dictionary_of_elements.get("download_size_MaxH")))

    #Main program
    searching_by_keywords_or_by_images=dictionary_of_elements.get("searching_by_keywords_or_by_images")
    print (searching_by_keywords_or_by_images)
    
    if searching_by_keywords_or_by_images=="keywords":
    
        for search_key in search_keys:
            image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
            image_urls = image_scrapper.find_image_urls()
            image_scrapper.save_images(image_urls)
    elif searching_by_keywords_or_by_images=="images":
        list_of_images_to_search_by = []
        path = os.getcwd()+"\\reverse_search"
        valid_images = [".jpg",".gif",".png",".jpeg"]
        for f in os.listdir(path):
            ext = os.path.splitext(f)[1]
            if ext.lower() not in valid_images:
                continue
            list_of_images_to_search_by.append(os.path.join(path,f))
        print (list_of_images_to_search_by)
        
        counter = 0
        for image in list_of_images_to_search_by:
        #rework this function
            image_scrapper = GoogleImageScraperReverseSearch(counter,image,webdriver_path,image_path,number_of_images,headless,min_resolution,max_resolution)
            image_urls = image_scrapper.find_image_urls()
            image_scrapper.save_images(image_urls)
            counter +=1
    #Release resources    
    #del image_scrapper