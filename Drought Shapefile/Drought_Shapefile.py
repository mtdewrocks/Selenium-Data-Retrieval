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

path = r'C:\Users\shawn\Documents\Python Scripts\Zip'
os.chdir(path)

op = webdriver.ChromeOptions()

op.add_experimental_option("prefs", {
  "download.default_directory": path,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True})



browser = webdriver.Chrome(options=op)
browser.get('https://droughtmonitor.unl.edu/data/shapefiles_m/USDM_current_M.zip')

time.sleep(5)
#

try:
    zipfile = zipfile.ZipFile(path + '\\USDM_current_M.zip')
    zipfile.extractall(path)
except FileNotFoundError:

    time.sleep(5)
    zipfile = zipfile.ZipFile(path + '\\USDM_current_M.zip')
    zipfile.extractall(path)
    

browser.close()
