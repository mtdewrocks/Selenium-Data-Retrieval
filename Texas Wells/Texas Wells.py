# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:31:08 2022

@author: shawn
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

import os
import glob
import pathlib
import requests
import zipfile
from io import BytesIO
from datetime import date

today = date.today().strftime('%Y%m%d')


path = r'C:\Users\shawn\Documents\Python Scripts\Zip'
os.chdir(path)

op = webdriver.ChromeOptions()

op.add_experimental_option("prefs", {
  "download.default_directory": path,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True})



browser = webdriver.Chrome(options=op)
browser.get('https://mft.rrc.texas.gov/link/4e9023eb-e4ee-45b8-81b7-aec1494c1e8e')
recordCount = browser.find_element_by_xpath("""//*[@id="fileTable:j_id__v_1"]/option[@value='1000']""").click()
selectAll = browser.find_element_by_class_name("ui-chkbox").click()
time.sleep(2)
selectAll = browser.find_element_by_class_name("ui-chkbox").click()
time.sleep(1)
selectAll = browser.find_element_by_id("j_id_3c:j_id_3c").click()
time.sleep(45)

try:
    zipfile = zipfile.ZipFile(path + '\documents_'+today+'.zip')
    zipfile.extractall(path)
except FileNotFoundError:
    try:
        time.sleep(30)
        zipfile = zipfile.ZipFile(path + '\documents_'+today+'.zip')
        zipfile.extractall(path)
    
    except:
        time.sleep(30)
        zipfile = zipfile.ZipFile(path + '\documents_'+today+'.zip')
        zipfile.extractall(path)

browser.close()

##Could easily extend to extract the rest of the files into a single folder, or individual folders