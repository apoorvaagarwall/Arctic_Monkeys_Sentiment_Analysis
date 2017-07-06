from selenium import webdriver 
from selenium.support.ui import WebDriverWait 
from selenium.support.by import By 
from selenium.support import ExpectedConditions as EC
from selenium.commonexceptions.ui import TimeoutException 

import pandas as pd 
import numpy as np 

import os, time 

driver= webdriver.Chrome(executable_path="C:/Users/1hp/Downloads/chromedriver.exe")
driver.get("http://www.azlyrics.com/a/arcticmonkeys.html")

title=[]
lyrics=[]

WebDriverWait(driver,100).until(
	EC.visibility_of_element_located((By.XPATH, '//*[@id="listAlbum"]/a')))
main= driver.find_elements_by_xpath('//*[@id="listAlbum"]/a')

for j in range(0, len(main)):
    WebDriverWait(driver,30).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="listAlbum"]/div')))
    main= driver.find_elements_by_xpath('//*[@id="listAlbum"]/a')
    
    if main[j].text in title:
        continue
        
    if main[j].get_attribute("id"):
        continue
        
    title.append(main[j].text)
    driver.get(main[j].get_attribute("href"))
    WebDriverWait(driver,30).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[5]")))
    lyrics.append(driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]').text)
    driver.back()
    time.sleep(1)

lyrics = pd.DataFrame({"title":title, "lyrics":lyrics})
lyrics.to_csv("arctic_monkeys.csv")