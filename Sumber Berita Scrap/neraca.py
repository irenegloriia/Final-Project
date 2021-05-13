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

driver.get('https://www.neraca.co.id/article/144126/tingkatkan-literasi-keuangan-amar-bank-ngopi-bareng-bersama-komunitas')
time.sleep(5)
list = []
box = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div')
paragraf = box.find_elements_by_tag_name('p')
title = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/h1').text
time = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/span[2]').text
link = driver.current_url

print('Judul = ' +title)
print('Waktu = ' +time)
print(link)
for n in range(len(paragraf)):
    print(paragraf[n].text)
    
driver.quit()