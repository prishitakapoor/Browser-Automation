# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 00:18:26 2018

@author: SMIT
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def browser_automation():
    driver=webdriver.Chrome("chromedriver")  #path of chromedriver
    driver.get("https://web.whatsapp.com")
    wait=WebDriverWait(driver,500)
    target='"SMIT JETHWA"' #friend name in double " "
    msg="Hello World!!" #message
    x_arg='//span[contains(@title,'+ target +')]'   
    target=wait.until(ec.presence_of_element_located((By.XPATH,x_arg)))
    target.click()
    
    inputBox=driver.find_element_by_class_name("_2S1VP")  #inspact Element and copy class name of message box
    for i in range(123):
        inputBox.send_keys(msg+Keys.ENTER)
        
browser_automation()
