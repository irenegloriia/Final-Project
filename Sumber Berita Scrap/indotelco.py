from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

myprofile = webdriver.FirefoxProfile('/Users/irenegloriia/Library/Application Support/Firefox/Profiles/egc4m9xh.stockbitScrap')
PATH = "/opt/homebrew/Cellar/geckodriver/0.29.0/bin/geckodriver"
driver = webdriver.Firefox(firefox_profile=myprofile ,executable_path=PATH)

driver.get('https://www.indotelko.com/read/1616543783/pasar-tunggu-realisasi-konsolidasi-isat-tri')
#driver.get('https://www.indotelko.com/read/1594184639/telkom-vonage')
time.sleep(5)
list = []
paragraf = driver.find_element_by_xpath("//div[@id='font_news']")
teks2 = paragraf.find_element_by_xpath('//*[@id="box_bj"]')
title = driver.find_element_by_xpath('//*[@id="title"]').text
link = driver.current_url
if (len(driver.find_elements_by_xpath("/html/body/div[1]/div[4]/div[1]/div[4]")) > 0 ): 
    time = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div[4]").text
else : 
    time = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[5]/div[1]/div[4]").text
print('Judul = ' +title)
print('Waktu = ' +time)
print(link)
print(paragraf.text.replace(teks2.text, ''))
driver.quit()