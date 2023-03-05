
#_*_coding: utf-8_*_

# .venv\scripts\activate
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process


# run in ps: chrome.exe -remote-debugging-port=9014 --user-data-dir="C:\Users\andrew\Documents\Projects\TikTokAPI\Selenium\Chrome_Test_Profile"


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import os
import sys
#import win32com.client as win32
import json
import time
import re

# start web browser
options=webdriver.ChromeOptions()
#options.add_argument('headless')
#options.setExperimentalOption() #'new List<string>() { "enable-automation" }'
options.add_experimental_option('excludeSwitches', ['load-extension', 'enable-automation'])
options.add_argument("--window-size=1,1")
#options.add_experimental_option('debuggerAddress','localhost:9014')
#options.setExperimentalOption('debuggerAddress','localhost:9014')
capa = DesiredCapabilities.CHROME
driver=webdriver.Chrome(chrome_options=options, desired_capabilities=capa)


def getArticle(URL):

    driver.get(URL)

    #ContinueBoolean = int(input("Enter 1 to continue: "))

    #time.sleep(10)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ui-ncbiinpagenav-1']")))

    pageSource = driver.page_source

    soup = BeautifulSoup(pageSource, 'html.parser')
    textWrapper = soup.find_all('div', class_='tsec sec')
    fullText = ''

    for paragraph in textWrapper:
        #print(paragraph.text)
        fullText = fullText + '\n' + paragraph.text
    
    #print(fullText)

    formattedJSON = {
        'article': fullText
    }

    # json_string = json.dumps(formattedJSON)

    #json_string = formattedJSON

    driver.quit()

    return(formattedJSON)
